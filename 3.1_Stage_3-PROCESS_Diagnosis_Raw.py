'''
Stage 3.1: Raw Data Diagnostics & Profiling Pipeline
'''

import pandas as pd
from utils import get_db_connection, run_diagnostics

print("Process 1/4: Initializing database connection...")
# ==========================================
# 1. ESTABLISH THE CONNECTION
# ==========================================
# Call the function from your new utils.py file
engine = get_db_connection()
if not engine:
    print("Exiting script due to connection failure.")
    exit()
print("Process 1/4 Complete: Database connection engine created.\n")


print("Process 2/4: Preparing table list...")
# ==========================================
# 2. DEFINE TABLES AND STORAGE
# ==========================================
# List of the tables we want to pull from the database
tables = [
    "customers", "orders", "products", 
    "order_items", "payments", "reviews"
]

# Dictionary to store all our downloaded DataFrames
# Example: later you can access the customers dataframe using dfs['customers']
dfs = {}
print("Process 2/4 Complete: Table list and storage dictionary prepared.\n")


print("Process 3/4: Fetching data from MySQL...")
# ==========================================
# 3. LOAD DATA INTO DICTIONARY
# ==========================================
# Loop through the tables, run the SQL query, and save to the dictionary
for table in tables:
    print(f"  -> Fetching table: '{table}'...")
    query = f"SELECT * FROM {table}"
    
    # Read the SQL query directly into a Pandas DataFrame using our SQLAlchemy engine
    dfs[table] = pd.read_sql(query, con=engine)
    print(f"  -> Successfully loaded '{table}' into memory.")

# Note: SQLAlchemy engines manage their own connection pools, 
# so we don't need to manually run conn.close() like we did with mysql.connector.
print("Process 3/4 Complete: All tables successfully loaded into the 'dfs' dictionary.\n")


print("Process 4/4: Running diagnostics on all loaded tables...")
# ==========================================
# 4. DIAGNOSTIC COMMANDS
# ==========================================
# Call the DRY (Don't Repeat Yourself) function from utils.py
run_diagnostics(dfs)
print("\n--- SCRIPT EXECUTION FULLY COMPLETE ---")

author = '''
=============================================================================
👨‍💻 Author: Animesh Sanghi
=============================================================================
Title:    Data Analyst | MBA '28 (Analytics & Data Science) MUJ
Phone:    9406570600
Email:    animeshsanghi.da@gmail.com
LinkedIn: https://www.linkedin.com/in/animeshsanghi-da/
GitHub:   https://github.com/animeshsanghi-da
=============================================================================
'''
print("\n\n\n", author, "\n")