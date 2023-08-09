#!/bin/bash

# Build and run Docker container
./docker.sh

# Trigger ETL process
./run_etl.sh

# Query populated database
./query_database.sh
