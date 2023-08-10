# ETL Pipeline with API Trigger
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
   cd etl-app

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
  4. **Code Flow:**
      * ETL Process(etl.py):
         * Data Extraction from CSV files
           * The pipeline ingests data from three CSV files: users.csv, user_experiments.csv, and compounds.csv.
           * These files contain information about users, their experiments, and the compounds involved.
         * Data Transformation:
           * The data from user_experiments.csv is transformed to derive features.
           * Features include:
            * Total experiments conducted by each user.
            * Average number of experiments per user.
            * The most commonly experimented compound.
         * Data Poupulation
           * Transformed data is loaded into a PostgreSQL database.
           * The average_experiments table stores user IDs and their average experiment counts.
           * The most_common_compound table stores the ID of the most commonly experimented compound.
      * Flask API(app.py):

        The Flask API serves as the command center for the ETL pipeline. It provides a mechanism to initiate the ETL process and showcases the integration of API technology with the ETL workflow.
        * A custom API endpoint (/trigger_etl) is defined using the Flask framework.
        * An HTTP POST request to this endpoint triggers the ETL process.
      * Dockerization:
        * Dockerize the application to ensure consistent deployment across different environments.
        * Utilize a Dockerfile to define the container environment and dependencies.
        * Use the Docker CLI to build and run the Docker container.
         
  5. **How to Run and Test:**
     * Build and run the Docker container by executing the following command:
       ```bash
       chmod +x docker.sh
       ./docker.sh
       
     * Initiate the ETL process by sending an HTTP POST request to the API endpoint. Use the following command:
       ```bash
       chmod +x run_etl.sh
       ./run_etl.sh
     * After the ETL process completes, you can query the populated database for the derived features. Run the following command:
       ```bash
       chmod +x query_database.sh
       ./query_database.sh
     * Created a shell script to run everything with one command:
       ```bash
       chmod +x run_app.sh
       ./run_app.sh

6. **Future Work**
   * Automated Testing: Develop comprehensive unit tests and integration tests to verify the correctness of each component in the ETL pipeline.
   * Logging and Monitoring:
      * Implement robust logging mechanisms to track the ETL pipeline's progress and identify potential issues.
      * Utilize monitoring tools to gain insights into the pipeline's health and performance.

**NOTE**

Make sure the path for data files, names of database and user credentials, and ports are changed accordingly
