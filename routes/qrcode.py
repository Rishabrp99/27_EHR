import io
import qrcode

from fastapi import FastAPI,APIRouter
from starlette.responses import StreamingResponse


router = APIRouter()

@router.get("/generate/{id}")
def generate(id: str):

    base_url = "http://localhost:8000/usershare/"

    img = qrcode.make(base_url + id)
    buf = io.BytesIO()
    img.save(buf)
    buf.seek(0) # important here!
    return StreamingResponse(buf, media_type="image/jpeg")

