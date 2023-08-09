#!/bin/bash

# Build the Docker image
docker build -t etl-app .

# Set the PostgreSQL database URL
export DB_URL="postgresql://user:passuser@8080:5432/postgres_db"

# Run the Docker container
docker run -d -p 8080:5432 --name etl-container etl-app