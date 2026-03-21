import cloudinary
import cloudinary.uploader
import os
from schemas.cloud import cloudPic
from fastapi import APIRouter

upload_router = APIRouter(
    prefix="/cloud_store"
)

cloudinary.config(
    cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key = os.getenv("CLOUDINARY_API_KEY"),
    api_secret = os.getenv("CLOUD_API_SECRET"),
    secure = True
)
@upload_router.post("upload/")
def upload_photo(data: cloudPic)-> str:
    file_bytes = data.file_bytes
    user_id = data.user_id
    result = cloudinary.uploader.upload(
        file_bytes,
        folder = f"hometownhub/avatars",
        public_id = f"user_{user_id}",
        overwrite = True,
        resource_type = "images",
        transformation = [
            {
                "width": 400,
                "height": 400,
                "crop": "fill",
                "gravity": "face",
                "quality": "auto",
                "fetch_format": "auto"
            }
        ]
    )
    return result["secure_url"]

def delete_pic(data):
    user_id= data.user_id
    public_id = f"hometownhub/avatars/user_{user_id}"
    cloudinary.uploader.destroy(public_id)