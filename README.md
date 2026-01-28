# Document Parsing Agent (KYC)- PAN card

## Overview
This project implements a **Document Parsing Agent** that extracts **structured KYC information** from **PAN Card** and **Aadhaar Card images** using **Google Gemini Flash**.  
The solution is exposed as a **POST API** built with **FastAPI** and returns extracted details in **JSON format**.

---

## Model Used
- **Model:** `models/gemini-flash-latest`
- **Platform:** Google AI Studio
- **SDK:** `google-genai`

**Reason for model selection:**
- Supports image + text (multimodal input)
- Fast inference suitable for real-time use
- Performs OCR and reasoning internally

---

## Tech Stack
- Python
- FastAPI
- Uvicorn
- Google Gemini Flash
- Pillow (image handling)

---

## Features
- Accepts PAN / Aadhaar **images**
- Extracts key fields using Gemini Flash
- Returns structured JSON response
- API-based design for easy integration

---

## API Details
POST /parse-kyc


### Input
- `document_type`: PAN or AADHAAR
- `file`: Image (jpg / png)

### Output
- JSON containing extracted KYC fields

---

## How to Run
```bash
pip install -r requirements.txt
python -m uvicorn app.main:app

Open Swagger UI:

http://127.0.0.1:8000/docs
### Endpoint
