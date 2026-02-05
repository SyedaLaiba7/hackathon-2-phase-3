"""Vercel serverless function entry point for FastAPI."""
from mangum import Mangum
from app.main import app

# Wrap FastAPI app with Mangum for AWS Lambda/Vercel compatibility
handler = Mangum(app, lifespan="off")

