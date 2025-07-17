import sys
sys.path.append('/home/ekanthsai/Desktop/PoC')  

from config import config  

from ctransformers import AutoModelForCausalLM
import mysql.connector

llm = AutoModelForCausalLM.from_pretrained(
    model_path_or_repo_id=".",  
    model_file="/home/ekanthsai/Desktop/PoC/models/llama-2-13b-ensemble-v5.Q5_K_M.gguf",  
    model_type="llama",
    gpu_layers=0
)

def interpret_query(user_query: str):
    prompt = f"Convert the following Natural Language query into an executable SQL query for the 'insurance_db' database. The table 'claims_data' contains columns like 'employer_id' and 'covered_amount'. {user_query}"

    sql_query = llm(prompt).strip()  
    print(f"Generated SQL query: {sql_query}")

    try:
        conn = config.get_db_connection()
        cursor = conn.cursor()
        cursor.execute(sql_query)
        results = cursor.fetchall()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error executing query: {err}")
        results = []

    return results

user_query = "Give me the average of the Employer_ID?"
results = interpret_query(user_query)

for row in results:
    print(row)