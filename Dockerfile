# Use Python 3.8 as the base image
FROM python:3.8

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the port
EXPOSE 5000

# Define the startup command
CMD ["python", "financial_api.py"]

# Include environment variables from the .env file in the image using the --env-file option
RUN set -o allexport; source $ENV_FILE; set +o allexport