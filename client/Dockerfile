# Use Python's official image
FROM python:3.9-slim

# Set working directory
WORKDIR /client

# Copy requirements.txt to the container
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy client files
COPY . .

# Command to run the client app
CMD ["python", "client.py"]
