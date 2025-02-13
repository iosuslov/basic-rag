"""Main application module."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from app.core.config import get_settings
from app.api.api_v1.api import api_router

settings = get_settings()

app = FastAPI(
    title=settings.APP_NAME,
    description="A basic web service built with FastAPI",
    version="0.1.0",
    debug=settings.DEBUG,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Welcome to the Basic Web Service",
        "docs": "/docs",
        "redoc": "/redoc",
        "api": settings.API_V1_STR,
    }


@app.on_event("startup")
async def startup_event():
    """Initialize application services."""
    logger.info("Starting up application...")


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup application services."""
    logger.info("Shutting down application...")
