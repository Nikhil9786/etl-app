# ETL Pipeline with API
This repository contains a simple ETL (Extract, Transform, Load) pipeline with an API trigger. The pipeline processes CSV files, derives features, and populates a PostgreSQL database table.

### Introduction
This project demonstrates the creation of a basic ETL pipeline using Python, Flask, Docker, and PostgreSQL. The primary objective is to extract data from CSV files, perform feature transformation, and load the processed data into a PostgreSQL database. The ETL process can be initiated via an API endpoint.

### Prerequisites
- Python 3.7+
- Docker
- PostgreSQL

### Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Nikhil9786/etl-app.git
   cd etl-api

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt

 3. **Database Configuration:**
    * Assuming PostgreSQL is installed, I created a database that will store the processed data using psql.
       ```bash
       CREATE DATABASE postgres_db;
       ```
    * To securely interact with password, it is essential to create user password
       ```bash
      CREATE USER user WITH PASSWORD 'passuser';
       ```
    * Granting appropriate permissions to user
       ```bash
      GRANT ALL PRIVILEGES ON DATABASE postgres_db TO user;
       ```
  4. 5. **Code Flow:**
      * ETL Process:
        * Load data from CSV files using the Pandas library
        * Derive features such as total experiments, average experiments, and most commonly experimented compound.
        * Use Pandas and SQLalchemy to upload the derived data to a PostgreSQL database table.
      * Flask API:
        * Create an API using the Flask framework.
        * Define a custom route (/trigger_etl) to trigger the ETL process via an HTTP POST request.
      * Dockerization:
        * Dockerize the application to ensure consistent deployment across different environments.
        * Utilize a Dockerfile to define the container environment and dependencies.
        * Use the Docker CLI to build and run the Docker container.
         
  5. **How to Run and Test:**
     * Build and run the Docker container by executing the following command:
       ```bash
       chmod +x run_etl.sh
       ./run_etl_container.sh
       
     * Initiate the ETL process by sending an HTTP POST request to the API endpoint. Use the following command:
       ```bash
       chmod +x run_etl.sh
       ./trigger_etl_services.sh
     * After the ETL process completes, you can query the populated database for the derived features. Run the following command:
       ```bash
       python query_database.py
