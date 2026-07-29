# Medicine Vision Backend Microservice

Computer Vision processing backend designed to integrate with **Base44** for shelf visual feature analysis and dynamic medicine image indexing.

## Features
- **Automatic Syncing:** Listens to Base44 webhooks on photo additions/deletions.
- **SIFT Feature Extraction:** Extracts visual keypoints using OpenCV.
- **Asynchronous Processing:** Non-blocking background task execution.

## Local Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/medicine-vision-backend.git](https://github.com/YOUR_USERNAME/medicine-vision-backend.git)
   cd medicine-vision-backend
