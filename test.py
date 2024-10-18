# ypthon file

# GITHUB_PAT - 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
# AWS_ACCESS_KEY - AKIAYZZGSY75A5HVL2EJ
# AWS_SECRET_KEY - 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
# STRIPE_KEY - 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

import pymysql

# Hardcoded RDS credentials
RDS_HOST = "database-12.cpk0awu2kyvt.us-east-1.rds.amazonaws.com"
RDS_PORT = 3306
RDS_USER = "admin"
RDS_PASSWORD = "mypassword"
RDS_DB_NAME = "mysql"

def connect_to_rds():
    try:
        # Establish connection to RDS
        connection = pymysql.connect(
            host=RDS_HOST,
            port=RDS_PORT,
            user=RDS_USER,
            password=RDS_PASSWORD,
            database=RDS_DB_NAME
        )
        print("Connected to RDS MySQL instance.")
        return connection
    except pymysql.MySQLError as e:
        print(f"Error connecting to RDS: {e}")
        return None

def fetch_data(connection):
    try:
        # Create a cursor object
        with connection.cursor() as cursor:
            # Execute a simple query
            cursor.execute("SELECT * FROM your_table LIMIT 10;")
            # Fetch and print the results
            result = cursor.fetchall()
            for row in result:
                print(row)
    except pymysql.MySQLError as e:
        print(f"Error executing query: {e}")
    finally:
        connection.close()

if __name__ == "__main__":
    # Connect to the RDS instance
    conn = connect_to_rds()
    if conn:
        # Fetch and print data
        fetch_data(conn)
