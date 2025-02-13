"""Health check endpoint for monitoring application status."""


from fastapi import APIRouter

from app.schemas import HealthResponse

router = APIRouter()


@router.get(
    "/health",
    response_model=HealthResponse,
    response_description="Health check response",
)
async def health_check() -> HealthResponse:
    """Health check endpoint."""
    return HealthResponse(status="healthy")
