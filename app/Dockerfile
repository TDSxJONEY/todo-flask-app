# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for caching layers)
COPY app/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all app files
COPY app/ .

# Expose Flask port
EXPOSE 5000

# Run the app
CMD ["python", "main.py"]
