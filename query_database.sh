#!/bin/bash

# Run queries on the populated database
echo "Querying the database..."

# Connect to the PostgreSQL database using psql
psql -h localhost -p 5432 -U user -d postgres_db -c "SELECT * FROM average_experiments;"

# Query the most common compound
psql -h localhost -p 5432 -U user -d postgres_db -c "SELECT * FROM most_common_compound;"

echo "Querying completed."