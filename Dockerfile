# Base image (lightweight Python)
FROM --platform=linux/amd64 python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy project files
COPY main.py requirements.txt ./
COPY input ./input
COPY output ./output

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command when container runs
CMD ["python", "main.py"]
