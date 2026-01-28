import json
from app.config import client, MODEL_NAME

def parse_document(image):
    prompt = """
You are a document understanding agent.

Tasks:
1. Identify the document type(government id).
2. Extract all fields visible in the document.
3. Return ONLY valid JSON.

JSON format:
{
  "document_type": "<identified type>",
  "fields": {
    "field_name": "value or null"
  }
}

Rules:
- Do not add explanation text
- If unsure, return null
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[image, prompt]
    )

    if not response or not response.text:
        return {
            "error": "Empty response from Gemini"
        }

    text = response.text.strip()

    # Defensive JSON extraction
    try:
        start = text.index("{")
        end = text.rindex("}") + 1
        return json.loads(text[start:end])
    except Exception as e:
        return {
            "error": "Failed to parse Gemini response",
            "raw_response": text
        }
