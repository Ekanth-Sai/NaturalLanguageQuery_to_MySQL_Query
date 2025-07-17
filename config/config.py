import mysql.connector

DB_CONFIG = {
    "host": "localhost", # Change as per the host requirements
    "user": "root", # Change as per the user requirements
    "password": "admin", #Change as per the password requirements
    "database": "insurance_db" # Change as per the database name requirements 
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)