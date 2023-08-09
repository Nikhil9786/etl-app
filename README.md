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
   git clone https://github.com/yourusername/etl-api.git
   cd etl-api

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt

 3. **Database Configuration:**
    * Assuming PostgreSQL is installed, I created a database that will store the processed data using psql.
    ``bash
    CREATE DATABASE postgres_db;
    * To securely interact with password, it is essential to create user password
      ```bash
      CREATE USER user WITH PASSWORD 'passuser';
    * Granting appropriate permissions to user
      ```bash
      GRANT ALL PRIVILEGES ON DATABASE postgres_db TO user;

  4. **How to Run:**
     * Build and run the Docker container by executing the following command:
       ```bash
       chmod +x run_etl.sh
       ./run_etl.sh
       
     * Initiate the ETL process by sending an HTTP POST request to the API endpoint. Use the following command:
       ```bash
       chmod +x run_etl.sh
       ./run_etl.sh
     * After the ETL process completes, you can query the populated database for the derived features. Run the following command:
       ```bash
       chmod +x query_database.sh
       ./query_database.sh

       
   5. **Code Flow:**
      * ETL Process:
        (i). Load data from CSV files using the Pandas library.
        (ii).Derive features such as total experiments, average experiments, and most commonly experimented compound.
Use Pandas and SQLalchemy to upload the derived data to a PostgreSQL database table.
Flask API:

Create an API using the Flask framework.
Define a custom route (/trigger_etl) to trigger the ETL process via an HTTP POST request.
Dockerization:

Dockerize the application to ensure consistent deployment across different environments.
Utilize a Dockerfile to define the container environment and dependencies.
Use the Docker CLI to build and run the Docker container.


### Data
You will find three CSV files in the `data`  directory:

- `users.csv`: Contains user data with the following columns: `user_id`, `name`, `email`,`signup_date`.

- `user_experiments.csv`: Contains experiment data with the following columns: `experiment_id`, `user_id`, `experiment_compound_ids`, `experiment_run_time`. The `experiment_compound_ids` column contains a semicolon-separated list of compound IDs.


- `compounds.csv`: Contains compound data with the following columns: `compound_id`, `compound_name`, `compound_structure`.


## Feature Derivation
From the provided CSV files, derive the following features:

1. Total experiments a user ran.
2. Average experiments amount per user.
3. User's most commonly experimented compound.

## Deliverables
Please provide the following in a GITHUB REPOSITORY.

1. A Dockerfile that sets up the environment for your application.
2. A requirements.txt file with all the Python dependencies.
3. A Python script that sets up the API and the ETL process.
4. A brief README explaining how to build and run your application, and how to trigger the ETL process.


Please also provide a script that builds, and runs the docker container. 
You should also provide a script that scaffolds how a user can run the ETL process. This can be `curl` or something else.
Finally, provide a script that queries the database and showcases that it has been populated with the desired features.


## Evaluation
Your solution will be evaluated on the following criteria:

Code quality and organization.
Proper use of Python and Docker.
Successful execution of the ETL process.
Accuracy of the derived features.
