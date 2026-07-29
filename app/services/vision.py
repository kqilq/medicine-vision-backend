import cv2
import numpy as np
import requests

class VisionService:
    def __init__(self):
        # Initialize SIFT detector (Patent feature extraction primitive)
        self.sift = cv2.SIFT_create()

    def extract_features_from_url(self, image_url: str):
        """Downloads image from URL and extracts keypoints + descriptors."""
        try:
            resp = requests.get(image_url, timeout=10)
            if resp.status_code != 200:
                print(f"Error: Unable to fetch image from {image_url}")
                return None

            # Decode raw image bytes to OpenCV grayscale format
            image_array = np.asarray(bytearray(resp.content), dtype=np.uint8)
            img = cv2.imdecode(image_array, cv2.IMREAD_GRAYSCALE)

            if img is None:
                print("Error: Image decoding failed.")
                return None

            # Compute SIFT visual descriptors
            keypoints, descriptors = self.sift.detectAndCompute(img, None)

            if descriptors is None:
                return []

            return descriptors.tolist()

        except Exception as e:
            print(f"Exception during feature extraction: {e}")
            return None

vision_service = VisionService()
