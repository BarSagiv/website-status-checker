# Use official Python runtime as a parent image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Install curl (needed for your app) and traceroute (for traceroute command)
RUN apt-get update && apt-get install -y curl traceroute && rm -rf /var/lib/apt/lists/*

# Copy requirements (if you had one) or just install Flask directly
RUN pip install flask

# Copy the app code and templates folder into the container
COPY app.py /app/
COPY templates /app/templates/

# Expose the port Flask runs on
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]


# אפשר להעלות לדוקרהאב רק אחרי שסיימנו את הסקריפט לפלאסק