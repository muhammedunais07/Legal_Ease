from fastapi import FastAPI
from routes import router


app = FastAPI(
    title="LegalEase - AI Legal Document Generator",
    description="AI-powered legal document generation API",
    version="1.0.0"
)


app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Welcome to LegalEase AI Legal Document Generator API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }