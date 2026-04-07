'''
Database Security & Connection Utility (utils.py)
'''
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import os
import getpass
import logging
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def get_db_connection(db_name="ecomm_analytics"):
    """Securely creates and returns a SQLAlchemy engine with a smart fallback and retry limit."""
    db_user = "root"
    db_host = "localhost"
    db_password = None
    max_attempts = 3   # maximum attempts set to 3
    
    # 1. Try to load the password from the .env file first
    if os.path.exists('.env'):
        load_dotenv()
        db_password = os.getenv("DB_PASSWORD")
        
    # 2. If no .env file exists, or the password wasn't found, trigger the manual prompt
    if not db_password:
        print("\n[NOTICE] Because you are not using a .env file, you have to enter the password manually.")
        print("If you want to execute the project without entering the password manually every time, establish a .env file.\n")
        db_password = getpass.getpass("Enter Database Password: ")
        
    # 3. Connection attempt loop (Max 3 tries)
    for attempt in range(max_attempts):
        try:
            # Create the connection engine
            engine = create_engine(f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}")
            
            # Testing the connection - This will fail if the password is wrong
            with engine.connect() as conn:
                logging.info("Successfully connected to the MySQL database.")
            return engine
            
        except SQLAlchemyError as e:
            attempts_left = max_attempts - 1 - attempt
            
            if attempts_left > 0:
                print(f"\n[WARNING] The password entered is wrong. Please enter the correct password. You only have {attempts_left} attempt(s) left.")
                # Ask for the password manually for the next loop iteration
                db_password = getpass.getpass("Enter Database Password: ")
            else:
                print("\n[ERROR] You have reached the limit of entering the correct password, try next time.")
                return None

def run_diagnostics(dfs_dict):
    print("\nProcess: Starting data diagnostics generation...\n")
    """Runs standard info, describe, and null checks on a dictionary of DataFrames."""
    # Loop through our dictionary to print diagnostics for each DataFrame cleanly
    for table_name, df in dfs_dict.items():
        print(f"\n=======================================================")
        print(f"          DIAGNOSTICS FOR: {table_name.upper()}")
        print(f"=======================================================")
        
        # Data Types & Memory
        print(f"\n--- 1. DATA TYPES & NON-NULL COUNTS ({table_name}.info) ---")
        # df.info() prints directly to the console, so it doesn't need a print() wrapper
        df.info()  
        print(f"--- {table_name}.info check complete ---\n")
        
        # Summary Statistics
        print(f"--- 2. STATISTICAL SUMMARY ({table_name}.describe) ---")
        # df.describe() returns a DataFrame string, so we MUST wrap it in print()
        print(df.describe())
        print(f"--- {table_name}.describe check complete ---\n")
        
        # Missing Values Check
        print(f"--- 3. MISSING VALUES COUNT ({table_name}).isnull().sum() ---")
        # isnull() creates a boolean mask, sum() adds up the Trues (missing values) per column
        # df.isnull().sum() counts missing values per column
        print(df.isnull().sum())
        print(f"--- {table_name}.isnull().sum() check complete ---\n")

        print("\nProcess: Diagnostics fully complete for " + table_name + "\n\n")

    print("Process 4/4 Complete: All diagnostics finished.")

'''
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