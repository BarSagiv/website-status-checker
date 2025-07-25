# Use official Python runtime as a parent image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Install curl and traceroute
RUN apt-get update && apt-get install -y curl traceroute && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY app.py /app/
COPY templates /app/templates/

# Expose the port Flask runs on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
