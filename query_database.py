import psycopg2

# Database connection settings
db_params = {
    "host": "localhost",
    "port": "5432",
    "database": "postgres_db",
    "user": "user",
    "password": "passuser"
}

def fetch_user_features():
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Fetch user features from the database
    query = """
        SELECT user_id, total_experiments, average_experiments, most_common_compound
        FROM user_features
    """
    cursor.execute(query)
    user_features = cursor.fetchall()

    cursor.close()
    connection.close()

    return user_features

if __name__ == '__main__':
    user_features = fetch_user_features()

    # Print fetched user features
    for user_id, total_experiments, average_experiments, most_common_compound in user_features:
        print(f"User ID: {user_id}")
        print(f"Total Experiments: {total_experiments}")
        print(f"Average Experiments: {average_experiments}")
        print(f"Most Common Compound: {most_common_compound}")
        print("----------")
