from fastapi import FastAPI
from app.routers import webhooks
from app.config import settings

app = FastAPI(title=settings.APP_NAME)

# Include API Routers
app.include_router(webhooks.router)

@app.get("/")
def health_check():
    return {"status": "healthy", "service": settings.APP_NAME}
