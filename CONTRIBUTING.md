# Contributing to Basic RAG Service

This document provides guidelines and instructions for contributing to the Basic RAG Service project.

## Development Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd basic-rag
   ```

2. **Set up Python environment**
   ```bash
   # Install Poetry if you haven't already
   curl -sSL https://install.python-poetry.org | python3 -

   # Install dependencies
   poetry install
   ```

3. **Set up pre-commit hooks**
   ```bash
   poetry run pre-commit install
   ```

## Development Process

1. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Follow the project's code style
   - Add tests for new functionality
   - Update documentation if needed

3. **Run quality checks**
   ```bash
   # Run all checks (linting, type checking, and tests)
   ./scripts/lint.py

   # Run only linting checks
   ./scripts/lint.py --lint-only

   # Run only tests
   ./scripts/lint.py --test-only
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: your meaningful commit message"
   ```

   Follow [Conventional Commits](https://www.conventionalcommits.org/) for commit messages:
   - `feat:` for new features
   - `fix:` for bug fixes
   - `docs:` for documentation changes
   - `refactor:` for code refactoring
   - `test:` for adding tests
   - `chore:` for maintenance tasks

5. **Push your changes and create a Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

## Code Quality Standards

### Code Style

- We use `ruff` for code formatting and linting
- Maximum line length is 88 characters
- Use type hints for all function arguments and return values
- Follow PEP 8 naming conventions

### Testing

- Write tests for all new functionality
- Maintain test coverage above 80%
- Tests should be in the `tests/` directory
- Use pytest fixtures for test setup

### Documentation

- Add docstrings to all public functions and classes
- Keep the README.md up to date
- Document API changes in the API documentation

## Running the Application

### Local Development

1. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

2. **Run the development server**
   ```bash
   poetry run uvicorn app.main:app --reload
   ```

3. **Access the API documentation**
   - OpenAPI UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

### Using Docker

1. **Build the Docker image**
   ```bash
   # Build the image
   docker build -t basic-rag .

   # Or using BuildKit for better performance
   DOCKER_BUILDKIT=1 docker build -t basic-rag .
   ```

2. **Run the container**
   ```bash
   # Run in development mode with hot reload
   docker run -it --rm \
     -p 8000:8000 \
     -v $(pwd):/app \
     -e ENVIRONMENT=development \
     basic-rag

   # Run in production mode
   docker run -d \
     -p 8000:8000 \
     -e ENVIRONMENT=production \
     basic-rag
   ```

3. **Running Tests in Docker**
   ```bash
   # Run all tests
   docker run --rm basic-rag ./scripts/lint.py

   # Run only unit tests
   docker run --rm basic-rag ./scripts/lint.py --test-only

   # Run only linting
   docker run --rm basic-rag ./scripts/lint.py --lint-only
   ```

4. **Best Practices**
   - Use multi-stage builds to keep images small
   - Don't run containers as root
   - Use `.dockerignore` to exclude unnecessary files
   - Pin base image versions for reproducibility
   - Use BuildKit for faster builds

## Continuous Integration / Continuous Deployment (CI/CD)

Our project uses GitHub Actions for CI/CD. The pipeline is configured in `.github/workflows/ci-cd.yml`.

### CI Pipeline

The CI pipeline runs automatically on:
- Push to `master` branch
- Push to `feature-*` branches
- Pull requests to these branches

It consists of the following jobs:

1. **Lint**
   - Runs Ruff for code formatting and linting
   - Performs type checking with MyPy

2. **Test** (runs after successful lint)
   - Runs pytest with coverage reporting
   - Coverage report is generated in XML format

3. **Deploy** (runs after successful test)
   - Only triggers on `master` branch
   - Handles deployment to production

### Required Status Checks

All pull requests must pass these checks before merging:
- ✓ Lint (ruff, mypy)
- ✓ Test (pytest with coverage)

## Getting Help

- Check existing issues and pull requests
- Create a new issue for bugs or feature requests
- Ask questions in the project's communication channels

## License

By contributing to this project, you agree that your contributions will be licensed under its license terms.
