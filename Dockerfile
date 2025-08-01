# Use official Python image
FROM python:3.11-slim

# Install Tesseract and other dependencies
RUN apt-get update && \
    apt-get install -y tesseract-ocr && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install Python packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5000

# Start the Flask app
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
