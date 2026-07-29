import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME: str = "Medicine Vision Backend"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() in ("true", "1")
    PORT: int = int(os.getenv("PORT", 8000))

settings = Settings()
