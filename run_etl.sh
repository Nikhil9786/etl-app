#!/bin/bash

# Run the ETL process
python etl.py

# Trigger the ETL process via the API
curl -X POST http://localhost:80/trigger-etl
