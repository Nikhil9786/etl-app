import pandas as pd
import psycopg2

def derive_features(user_experiments_df, compounds_df):
    user_experiments_df['total_experiments'] = user_experiments_df['experiment_compound_ids'].apply(lambda x: len(x.split(';')))
    
    avg_experiments_per_user = user_experiments_df.groupby('user_id')['total_experiments'].mean().reset_index()
    avg_experiments_per_user.rename(columns={'total_experiments': 'average_experiments'}, inplace=True)

    compound_counts = user_experiments_df['experiment_compound_ids'].str.split(';').explode().value_counts()
    most_common_compound_id = compound_counts.index[0]

    most_common_compound_name = compounds_df.loc[compounds_df['compound_id'] == most_common_compound_id, 'compound_name'].values[0]
    
    return avg_experiments_per_user, most_common_compound_name

def upload_data_to_database(conn, data, table_name, columns):
    cursor = conn.cursor()

    for index, row in data.iterrows():
        values = ", ".join([f"'{row[col]}'" for col in columns])
        cursor.execute(f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({values})")

    conn.commit()
    cursor.close()

def main():
    # Load CSV files
    users_df = pd.read_csv("/Users/ujain/Downloads/backend_takehome/data/users.csv")
    user_experiments_df = pd.read_csv("/Users/ujain/Downloads/backend_takehome/data/user_experiments.csv")
    compounds_df = pd.read_csv("/Users/ujain/Downloads/backend_takehome/data/compounds.csv")

    # Derive features
    avg_experiments_per_user, most_common_compound_name = derive_features(user_experiments_df, compounds_df)

    # Connect to PostgreSQL database
    conn = psycopg2.connect(
        dbname="postgres_db",
        user="user",
        password="userpass",
        host="localhost",
        port="5432"
    )

    # Upload processed data to PostgreSQL
    upload_data_to_database(conn, avg_experiments_per_user, "average_experiments", ["user_id", "average_experiments"])
    upload_data_to_database(conn, pd.DataFrame({"compound_name": [most_common_compound_name]}), "most_common_compound", ["compound_name"])

    # Close database connection
    conn.close()

if __name__ == "__main__":
    main()
