FROM python:3.10-slim

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    aria2 \
    gcc \
    libffi-dev \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip setuptools wheel

# Copy requirements first
COPY master.txt requirements.txt

# Install python deps
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

CMD ["python", "main.py"]

