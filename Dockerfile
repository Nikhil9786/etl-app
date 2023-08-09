# Use an official Python runtime as the base image
FROM python:3.7-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app/

# Expose port 5000 to the outside world
EXPOSE 8080

# Define environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8080
ENV DATABASE_URL=postgresql://user:passuser@8080:5432/postgres_db

# Run the API when the container launches
CMD ["flask", "run"]
