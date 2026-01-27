from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.gemini_service import extract_kyc_data
from app.utils.file_utils import load_image

router = APIRouter()

@router.post("/parse-kyc")
async def parse_kyc(
    document_type: str = Form(...),
    file: UploadFile = File(...)
):
    document_type = document_type.upper().strip()

    if document_type not in ["PAN", "AADHAAR"]:
        raise HTTPException(status_code=400, detail="Invalid document type")

    if file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="PDF not supported. Upload image only."
        )

    file_bytes = await file.read()

    try:
        image = load_image(file_bytes)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid image")

    return extract_kyc_data(document_type, image)
