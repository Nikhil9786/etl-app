import pandas as pd
import psycopg2

def derive_features(users_df, user_experiments_df, compounds_df):
    # Derive features
    user_experiments_df['total_experiments'] = user_experiments_df['experiment_compound_ids'].apply(lambda x: len(x.split(';')))
    
    avg_experiments_per_user = user_experiments_df.groupby('user_id')['total_experiments'].mean().reset_index()
    avg_experiments_per_user.rename(columns={'total_experiments': 'average_experiments'}, inplace=True)

    most_common_compound = user_experiments_df['experiment_compound_ids'].str.split(';').explode().value_counts().idxmax()
    
    return avg_experiments_per_user, most_common_compound

def upload_to_database(df, conn):
    cursor = conn.cursor()

    # Upload average experiments per user
    for index, row in df.iterrows():
        cursor.execute(
            "INSERT INTO average_experiments (user_id, average_experiments) VALUES (%s, %s)",
            (row['user_id'], row['average_experiments'])
        )

    # Upload most common compound
    cursor.execute(
        "INSERT INTO most_common_compound (compound_id) VALUES (%s)",
        (df['most_common_compound'],)
    )

    conn.commit()
    cursor.close()

def main():
    # Load CSV files
    users_df = pd.read_csv("/Users/ujain/Downloads/backend_takehome/data/users.csv")
    user_experiments_df = pd.read_csv("/Users/ujain/Downloads/backend_takehome/data/user_experiments.csv")
    compounds_df = pd.read_csv("/Users/ujain/Downloads/backend_takehome/data/compounds.csv")

    # Derive features
    avg_experiments_per_user, most_common_compound = derive_features(users_df, user_experiments_df, compounds_df)

    # Connect to PostgreSQL database
    conn = psycopg2.connect(
        dbname="postgres_db",
        user="user",
        password="userpass",
        host="localhost",
        port="5432"
    )

    # Upload processed data to PostgreSQL
    upload_to_database(avg_experiments_per_user, most_common_compound, conn)

    # Close database connection
    conn.close()

if __name__ == "__main__":
    main()
