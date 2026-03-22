import cloudinary
import cloudinary.uploader
import os
from fastapi import APIRouter, UploadFile, File, HTTPException

upload_router = APIRouter(
    prefix="/cloud_store"
)

cloudinary.config(
    cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key = os.getenv("CLOUDINARY_API_KEY"),
    api_secret = os.getenv("CLOUDINARY_API_SECRET"),
    secure = True
)
@upload_router.post("/upload")
async def upload_photo(file:UploadFile = File(), user_id: int=0)-> str:
    allowed = {"image/jpeg", "image/png", "image/webp", "image/gif"}
    if file.content_type not in allowed:
        raise HTTPException(status_code=400, detail="File type not allowed.")
    file_bytes = await file.read()
    result = cloudinary.uploader.upload(
        file_bytes,
        folder        = "hometownhub/avatars",
        public_id     = f"user_{user_id}",
        overwrite     = True,
        resource_type = "image", 
        transformation = [{
            "width": 400, "height": 400,
            "crop": "fill", "gravity": "face",
            "quality": "auto", "fetch_format": "auto"
        }]
    )
    return {"photo_url": result["secure_url"]}

def delete_pic(user_id:int):
    user_id= user_id
    public_id = f"hometownhub/avatars/user_{user_id}"
    cloudinary.uploader.destroy(public_id)
    return {"message": f"Deleted photo for user {user_id}"}