# Document Parsing Agent (KYC)

## Overview
This project implements a **Document Parsing Agent** that extracts **structured KYC information** from documents(images or pdf) using **Google Gemini Flash**.  
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
fastapi
uvicorn
python-multipart
pillow
python-dotenv
google-genai
pymupdf

---

## Features
- Accepts  **image** and **pdf**
- Extracts key fields using Gemini Flash
- Returns structured JSON response
- API-based design for easy integration

---

## API Details
POST /parse-kyc


### Input

- `file`: Image (jpg / png / jpeg) and File(pdf)

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
