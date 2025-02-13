# Basic RAG Service

A Retrieval-Augmented Generation (RAG) web service built with FastAPI, following modern Python best practices.

## Features

- FastAPI-based REST API for RAG operations
- Configuration management with pydantic
- Logging with loguru
- Testing with pytest
- Code quality tools (black, flake8, mypy)
- CI/CD ready
- Pre-commit hooks
- Docker support

## Requirements

- Python 3.8+
- Poetry

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd basic-rag
```

2. Install dependencies:
```bash
poetry install
```

3. Set up pre-commit hooks:
```bash
poetry run pre-commit install
```

4. Create `.env` file:
```bash
cp .env.example .env
```

## Development

1. Run the development server:
```bash
poetry run uvicorn app.main:app --reload
```

2. Visit the API documentation:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Testing

Run tests:
```bash
poetry run pytest
```

Run tests with coverage:
```bash
poetry run pytest --cov=app tests/
```

## Project Structure

```
.
├── app/
│   ├── api/             # API routes
│   ├── core/            # Core functionality
│   ├── schemas/         # Pydantic models
│   └── services/        # Business logic
├── tests/               # Test files
├── docs/                # Documentation
├── .env                 # Environment variables
├── .pre-commit-config.yaml
├── pyproject.toml       # Project dependencies
└── README.md
```

## License

This project is licensed under the terms of the MIT license.
