# Basic Web Service

A basic web service built with FastAPI, Poetry, and Docker.

## Prerequisites

- Python 3.8 or higher
- Poetry
- Docker

## Development Setup

1. Install dependencies:
```bash
poetry install
```

2. Run the development server:
```bash
poetry run uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000

## Docker Setup

1. Build the Docker image:
```bash
docker build -t basic-web-service .
```

2. Run the container:
```bash
docker run -p 8000:8000 basic-web-service
```

## API Documentation

Once the service is running, you can access:
- API documentation: http://localhost:8000/docs
- Alternative documentation: http://localhost:8000/redoc

## Endpoints

- GET `/`: Welcome message
- GET `/health`: Health check endpoint
