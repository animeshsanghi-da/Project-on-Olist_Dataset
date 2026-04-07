'''
Stage 3.3: Cleaned Data Validation & Diagnostics
'''

import pandas as pd
from utils import get_db_connection, run_diagnostics

print("Process: Libraries imported successfully.")

# ==========================================
# 1. DATABASE CONNECTION
# ==========================================
print("\nProcess: Attempting to connect to the database...")
# Call the function from your new utils.py file
engine = get_db_connection()

if not engine:
    print("Exiting script due to connection failure.")
    exit()
    
print("Process Complete: Database connection engine created.\n")

# ==========================================
# 2. DEFINE TABLES TO PULL
# ==========================================
print("\nProcess: Defining the list of tables to extract...")

tables = [
    "customers_cleaned", "orders_cleaned", "products_cleaned", 
    "order_items_cleaned", "payments_cleaned", "reviews_cleaned",
    "master_analytical_view"
]

# Dictionary to store all our DataFrames. 
# Key = table name (string), Value = DataFrame
dfs = {}
print(f"Process: {len(tables)} tables identified for extraction.")

# ==========================================
# 3. DATA EXTRACTION LOOP
# ==========================================
print("\nProcess: Starting data extraction from MySQL...")

# Loop through our list of table names
for table in tables:
    print(f"  -> Extracting table: {table}...")
    
    # Dynamically build the SQL query for each table
    query = f"SELECT * FROM {table}"
    
    # Read the SQL query results directly into a pandas DataFrame and store in dictionary
    dfs[table] = pd.read_sql(query, engine)
    
    print(f"  -> Successfully loaded '{table}' into memory.")

print("Process: All tables extracted successfully.")

# ==========================================
# 4. CLOSE CONNECTION
# ==========================================
print("\nProcess: Closing database connection...")

# Safely close the SQLAlchemy connection pool
engine.dispose()
print("Process: Database connection closed.")

# ==========================================
# 5. RUN DIAGNOSTICS
# ==========================================
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