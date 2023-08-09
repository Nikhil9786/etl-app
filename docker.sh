#!/bin/bash

# Build the Docker image
docker build -t etl-app .

# Run the Docker container
docker run -p 5000:80 etl-app
