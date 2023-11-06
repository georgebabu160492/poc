# Use the official Python image as a base image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /code

# Copy the rest of the application code
COPY . /code/
# Install dependencies
# COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
# RUN pip install fastapi uvicorn



# Expose the port the application runs on
EXPOSE 8000

# Start the FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
