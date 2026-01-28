from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.gemini_service import parse_document
from app.utils.file_utils import load_image_from_bytes, pdf_to_images

router = APIRouter()

@router.post("/parse-document")
async def parse_document_api(file: UploadFile = File(...)):
    filename = file.filename.lower()
    file_bytes = await file.read()

    results = []

    # IMAGE INPUT
    if filename.endswith((".jpg", ".jpeg", ".png")):
        image = load_image_from_bytes(file_bytes)
        data = parse_document(image)
        results.append({
            "page": 1,
            "data": data
        })

    # PDF INPUT
    elif filename.endswith(".pdf"):
        images = pdf_to_images(file_bytes)
        for idx, image in enumerate(images):
            data = parse_document(image)
            results.append({
                "page": idx + 1,
                "data": data
            })

    else:
        raise HTTPException(status_code=400, detail="Unsupported file format")

    return {
        "total_pages": len(results),
        "results": results
    }
