# Use an official Python runtime as the base image
FROM python:3.8

# Set the working directory to /api
WORKDIR /api

# Copy the current directory contents into the container at /api
COPY . /api

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV FLASK api

# Run app.py when the container launches
CMD ["python", "app.py"]