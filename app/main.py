"""Main application module."""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from app.api.v1.router import api_router
from app.core.config import get_settings
from app.schemas import RootResponse

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Lifespan events handler."""
    # Startup
    logger.info("Starting up application...")
    yield
    # Shutdown
    logger.info("Shutting down application...")


app = FastAPI(
    title=settings.APP_NAME,
    description="A basic web service built with FastAPI",
    version="0.1.0",
    debug=settings.DEBUG,
    lifespan=lifespan,
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


@app.get(
    "/",
    response_model=RootResponse,
    response_description="Root endpoint response",
)
async def root() -> RootResponse:
    """Root endpoint."""
    return RootResponse(message="Welcome to the Basic RAG Service", docs="/docs")
