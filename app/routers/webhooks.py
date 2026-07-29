from fastapi import APIRouter, BackgroundTasks, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.services.vision import vision_service
from app.services.storage import feature_store

router = APIRouter(prefix="/api/webhooks", tags=["Webhooks"])

class PhotoUploadPayload(BaseModel):
    medicine_id: str
    photo_id: str
    image_url: str

class PhotoDeletePayload(BaseModel):
    medicine_id: str
    photo_id: Optional[str] = None

def process_image_background(medicine_id: str, photo_id: str, image_url: str):
    descriptors = vision_service.extract_features_from_url(image_url)
    if descriptors is not None:
        feature_store.add_photo_features(medicine_id, photo_id, descriptors)

@router.post("/medicine-photo/index")
async def index_photo(payload: PhotoUploadPayload, background_tasks: BackgroundTasks):
    """Triggered by Base44 on Photo Upload."""
    background_tasks.add_task(
        process_image_background,
        payload.medicine_id,
        payload.photo_id,
        payload.image_url
    )
    return {"status": "processing", "medicine_id": payload.medicine_id, "photo_id": payload.photo_id}

@router.delete("/medicine-photo/delete")
async def delete_photo(payload: PhotoDeletePayload):
    """Triggered by Base44 on Photo Delete."""
    success = feature_store.remove_photo(payload.medicine_id, payload.photo_id)
    if not success:
        raise HTTPException(status_code=404, detail="Medicine or Photo ID not found")
    return {"status": "success", "medicine_id": payload.medicine_id, "photo_id": payload.photo_id}
