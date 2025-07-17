import mysql.connector 
import pandas as pd
import math

init_conn = mysql.connector.connect(
    host = "localhost",
    user = "root", # Change as per your system mysql
    password = "admin" # Change as per your system mysql
)

initial_cursor = init_conn.cursor()

initial_cursor.execute("CREATE DATABASE IF NOT EXISTS insurance_db")
initial_cursor.close()
init_conn.close()

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "admin",
    "database": "insurance_db"
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()


create_table_query = """
CREATE TABLE IF NOT EXISTS claims_data (
    Employer_ID INT,
    Employer_Name VARCHAR(255),
    Claim_Status VARCHAR(255),
    Claim_Type VARCHAR(255),
    Service_Start_Date DATE,
    Service_End_Date DATE,
    Provider_NPI INT,
    Place_of_Service INT,
    CPT_Procedure VARCHAR(255),
    Diagnosis_1 VARCHAR(255),
    Claim_Paid_Date DATE,
    Covered_Amount FLOAT,
    Plan_Paid_Amount FLOAT,
    Patient_SSN VARCHAR(255),
    In_Out_ER VARCHAR(255),
    Claim_Cause VARCHAR(255),
    Benefit_Code VARCHAR(255),
    Network VARCHAR(255),
    Provider_Name VARCHAR(255),
    Provider_Paid_Name VARCHAR(255),
    Charged_Amount FLOAT,
    UCR FLOAT,
    CPT_Modifier VARCHAR(255),
    Diagnosis_2 VARCHAR(255),
    Diagnosis_3 VARCHAR(255),
    Diagnosis_4 VARCHAR(255),
    Diagnosis_5 VARCHAR(255),
    Member_Deductible_Amount FLOAT,
    Member_OOP_Amount FLOAT,
    Member_Copay_Amount FLOAT,
    Claim_Number VARCHAR(255),
    Claim_Received_Date DATE,
    Claim_Entry_Date DATE,
    Adjuster VARCHAR(255),
    Document_Number VARCHAR(255),
    Sequence INT,
    Check_Number VARCHAR(255),
    Benefits_Assigned VARCHAR(255),
    Revenue_Code VARCHAR(255),
    Provider_EIN VARCHAR(255),
    Provider_Paid_NPI VARCHAR(255),
    Provider_Paid_Zip_Code VARCHAR(255),
    Unique_Patient_ID VARCHAR(255),
    Location_Code VARCHAR(255),
    Sub_Group_Code VARCHAR(255),
    Plan_Code VARCHAR(255)
);
"""

cursor.execute(create_table_query)

df = pd.read_csv("data/XYZ_10L.csv")
df = df.where(pd.notnull(df), None)

#print(len(df.columns))
#print(df.columns.tolist())

date_col = [
    "Service_Start_Date",
    "Service_End_Date",
    "Claim_Paid_Date",
    "Claim_Received_Date",
    "Claim_Entry_Date"
]

for col in date_col:
    df[col] = pd.to_datetime(df[col]).dt.strftime("%Y-%m-%d")

for i, row in df.iterrows():
    safe_row = [None if (isinstance(x, float) and math.isnan(x)) else x for x in row]
    cursor.execute(
        """
        INSERT INTO claims_data VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, safe_row
    )

conn.commit()
cursor.close()
conn.close()