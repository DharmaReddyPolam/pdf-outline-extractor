FROM --platform=linux/amd64 python:3.10-slim

WORKDIR /app

# Copy project files
COPY main.py requirements.txt ./
COPY input ./input
COPY output ./output

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
