# Use an official Python image as the base image
FROM python:3.9-alpine

# Set the working directory within the container
WORKDIR /app

# Copy the Python application code to the container
COPY . /app

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Define the command to run the application
CMD ["python", "app.py"]