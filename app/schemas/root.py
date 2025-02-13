"""Root endpoint response schemas."""

from pydantic import BaseModel


class RootResponse(BaseModel):
    """Root endpoint response schema."""

    message: str
    docs: str
