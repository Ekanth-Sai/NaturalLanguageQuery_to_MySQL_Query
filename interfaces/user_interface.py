import sys
sys.path.append('/home/ekanthsai/Desktop/PoC')  

import streamlit as st
from interfaces.query_interpreter import interpret_query

st.title("Insurance Claim Query System")

st.markdown("Enter a Natural Language Query to get converted to SQL query")

user_query = st.text_input("Enter your query: ")

if st.button("Submit Query"):
    if user_query:
        try:
            results = interpret_query(user_query)
            st.write(f"SQL Query Generated: {results[0]}")

            st.write("Results: ")

            for row in results:
                st.write(row)
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a query") 
