import json
from PIL import Image
from app.config import client, MODEL_NAME


def extract_kyc_data(document_type: str, image: Image.Image):
    if document_type == "PAN":
        schema = {
            "document_type": "PAN",
            "name": None,
            "father_name": None,
            "date_of_birth": None,
            "pan_number": None
        }
    else:
        schema = {
            "document_type": "AADHAAR",
            "name": None,
            "date_of_birth": None,
            "gender": None,
            "aadhaar_number": None,
            "address": None
        }

    prompt = f"""
You are a KYC document parsing agent.

Extract details from the given {document_type} card image.
Return ONLY valid JSON.
If a field is missing, keep it null.

Schema:
{json.dumps(schema, indent=2)}
"""

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=[image, prompt]
        )

        if not response or not response.text:
            return {"error": "Empty response from Gemini"}

        text = response.text.strip()

        start = text.find("{")
        end = text.rfind("}") + 1

        return json.loads(text[start:end])

    except Exception as e:
        return {
            "error": "Gemini processing failed",
            "exception": str(e)
        }
