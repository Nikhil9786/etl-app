#!/bin/bash

# Build the Docker image
docker build -t etl-app .

# Run the Docker container
docker run -p 5434:80 etl-app