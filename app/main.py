from fastapi import FastAPI
from app.routes.parse import router as parse_router

app = FastAPI(title="KYC Document Parsing Agent")

app.include_router(parse_router)

@app.get("/")
def health():
    return {"status": "running"}
