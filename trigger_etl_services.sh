#!/bin/bash

# Define the API endpoint URL
export API_URL="postgresql://user:passuser@localhost:5432/postgres_db"

# Make a POST request to trigger the ETL process
#curl -X POST http://localhost:5432/api/trigger_etl

#echo "ETL process triggered."

response=$(curl -X POST http://localhost:5432/api/trigger_etl 2>/dev/null)

# Check the exit status of curl
if [ $? -eq 0 ]; then
    echo "ETL process triggered successfully."
else
    echo "Failed to trigger ETL process."
fi