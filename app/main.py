from fastapi import FastAPI
from app.api.routes import router as api_router
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create the FastAPI app
app = FastAPI(title="Student Registry API")

# Health check route
@app.get("/")
def read_root():
    return {"message": "Student Registry API is up and running!"}

# Include all API routes
app.include_router(api_router, prefix="/api")
