# Use Python 3.8 slim image as base
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Install poetry
RUN pip install poetry

# Copy the entire project
COPY . .

# Configure poetry to not create virtual environment inside container
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --only main --no-interaction --no-ansi

# Expose port
EXPOSE 8000

# Run the application
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
