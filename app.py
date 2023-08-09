from flask import Flask, request, jsonify
from collections import Counter
import csv
import pandas as pd
import psycopg2

app = Flask(__name__)

DATABASE_URL = "postgresql://user:passuser@8080:5432/postgres_db"

def load_csv(file_path):
    data = pd.read_csv(file_path)
    return data

def etl():
    # Load CSV files
    # Process files to derive features
    # Upload processed data into a database
    # Create a dictionary to store user information and their experiments
    users_data = load_csv('data/users.csv')
    experiments_data = load_csv('data/user_experiments.csv')
    compounds_data = load_csv('data/compounds.csv')

    user_info = {}
    
    # Process user experiments and compound data
    for experiment in experiments_data:
        user_id = experiment['user_id']
        compound_ids = experiment['experiment_compound_ids'].split(';')
        
        if user_id not in user_info:
            user_info[user_id] = {
                'total_experiments': 0,
                'experiment_count': Counter(),
                'most_common_compound': None
            }
        
        user_info[user_id]['total_experiments'] += 1
        user_info[user_id]['experiment_count'].update(compound_ids)
    
    # Calculate average experiments and most commonly experimented compound
    for user_id, info in user_info.items():
        total_experiments = info['total_experiments']
        experiment_count = info['experiment_count']
        
        average_experiments = total_experiments / len(experiments_data)
        most_common_compound, _ = experiment_count.most_common(1)[0]
        
        user_info[user_id]['average_experiments'] = average_experiments
        user_info[user_id]['most_common_compound'] = most_common_compound
    
    return user_info
    pass


# Your API that can be called to trigger your ETL process
@app.route('/trigger_etl', methods=['POST'])
def trigger_etl():
    # Trigger your ETL process here
    try:
        # Process data
        processed_data = etl()
        
        # Insert processed data into the PostgreSQL database
        connection = psycopg2.connect(DATABASE_URL)
        cursor = connection.cursor()
        # Perform SQL INSERT operations here using the processed_data
        for user_id, info in processed_data.items():
            total_experiments = info['total_experiments']
            average_experiments = info['average_experiments']
            most_common_compound = info['most_common_compound']

            # SQL INSERT statement
            insert_query = """
                INSERT INTO user_features (user_id, total_experiments, average_experiments, most_common_compound)
                VALUES (%s, %s, %s, %s)
            """
            data = (user_id, total_experiments, average_experiments, most_common_compound)
            cursor.execute(insert_query, data)
        
        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"message": "ETL process completed successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
