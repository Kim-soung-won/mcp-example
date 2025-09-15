# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Install uv
RUN pip install uv
RUN pip install --upgrade pip

# Copy dependency management files
COPY pyproject.toml uv.lock ./

# Install dependencies from uv.lock
RUN uv pip install --system --frozen
ENV PATH="/root/.local/bin:${PATH}"

# Copy the application code
COPY server.py ./

# Expose the port the app runs on (assuming 8000)
EXPOSE 8000

# Run the application
CMD ["python", "server.py"]
