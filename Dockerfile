# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=True
ENV APP_HOME=/app

# Set the working directory
WORKDIR $APP_HOME

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 8080 for Cloud Run
EXPOSE 8080

# Define environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PORT=8080

# Run gunicorn when the container launches
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
