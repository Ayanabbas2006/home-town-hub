from pydantic import BaseModel

class cloudPic(BaseModel):
    file_byte: bytes
    user_id: int

class deletePic(BaseModel):
    user_id: int