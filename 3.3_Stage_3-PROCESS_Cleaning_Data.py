'''
Stage 3.2: Data Cleaning & Feature Engineering Pipeline
'''

import pandas as pd
import numpy as np
from utils import get_db_connection

# *****************************************************************************
# 0. DATABASE CONNECTION SETTINGS
# *****************************************************************************
print("*"*40, "\n0. DATABASE CONNECTION SETTINGS\n", "*"*40)

# Call the function from your new utils.py file
engine = get_db_connection()
if not engine:
    print("Exiting script due to connection failure.")
    exit()
print("Process 1/4 Complete: Database connection engine created.\n")

# *****************************************************************************
# 1. DATA LOADING AND INITIAL CLEANING
# *****************************************************************************
print("*"*40, "\n1. DATA LOADING AND INITIAL CLEANING\n", "*"*40)

# ==========================================
# 1.1. DATA LOADING
# ==========================================
# List of all tables we need to extract from the MySQL database
tables = ["customers", "orders", "products", "order_items", "payments", "reviews"]
# Initialize an empty dictionary to hold our dataframes
dfs = {}

print("Process started: Loading tables from MySQL database...")
# Loop through the table list and query all data for each one
for table in tables:
    print(f"  -> Fetching table: {table}...")
    # SQL query to select everything from the current table
    query = f"SELECT * FROM {table}"
    # Read the SQL query results directly into a pandas DataFrame and store it in the dictionary
    dfs[table] = pd.read_sql(query, engine)
    print(f"  -> Successfully loaded {table} ({len(dfs[table])} rows).")
print("Process complete: All tables loaded successfully.\n")

print("Process started: Extracting all dataframes for cleaning...")
# Extract each dataframe from the dictionary into its own dedicated variable.
# Using .copy() ensures these are independent objects, preventing 'SettingWithCopy' warnings later.
orders = dfs['orders'].copy()
products = dfs['products'].copy() 
customers = dfs['customers'].copy()
order_items = dfs['order_items'].copy()
payments = dfs['payments'].copy()
reviews = dfs['reviews'].copy()
print("Process complete: All dataframes extracted.\n")

# ==========================================
# 1.2. CLEANING THE ORDERS TABLE
# ==========================================
print("Process started: Cleaning missing delivery and approval dates in 'orders'...")
# Remove rows where the item was never delivered to the customer (essential for delivery analysis)
orders.dropna(subset=['order_delivered_customer_date'], inplace=True)
# If an order lacks an approval timestamp, backfill it using the purchase timestamp
orders['order_approved_at'] = orders['order_approved_at'].fillna(orders['order_purchase_timestamp'])
# If the carrier delivery date is missing, backfill it using the final customer delivery date
orders['order_delivered_carrier_date'] = orders['order_delivered_carrier_date'].fillna(orders['order_delivered_customer_date'])
print(f"Process complete: Orders cleaned. New count: {len(orders)}.\n")

# ==========================================
# 1.3. CLEANING THE PRODUCTS TABLE
# ==========================================
print("Process started: Cleaning missing metrics and dimensions in 'products'...")
# List of columns where a missing value logically means "zero" (e.g., no description length)
cols_to_fill_zero = ['product_name_lenght', 'product_description_lenght', 'product_photos_qty']
# Fill the NaNs in these specific columns with 0
products.fillna({col: 0 for col in cols_to_fill_zero}, inplace=True)

# List of physical dimension columns necessary for logistics calculations
cols_to_drop_na = ['product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm']
# Drop rows that are missing these critical physical dimensions
products.dropna(subset=cols_to_drop_na, inplace=True)
print(f"Process complete: Products cleaned. New count: {len(products)}.\n")

# ==========================================
# 1.4. CLEANING THE REVIEWS TABLE
# ==========================================
print("Process started: Standardizing empty strings in 'reviews'...")
# FIX: Use string methods to strip whitespace, then replace empty/literal "nan" with true np.nan 
# This standardizes missing textual data so pandas can properly identify it as 'null' later
reviews['review_comment_message'] = reviews['review_comment_message'].astype(str).str.strip().replace(['', 'nan', 'None'], np.nan)
reviews['review_comment_title'] = reviews['review_comment_title'].astype(str).str.strip().replace(['', 'nan', 'None'], np.nan)
print("Process complete: Empty strings converted to NaN in reviews.\n")

# *****************************************************************************
# 2. CORRECTING DATA TYPES
# *****************************************************************************
print("*"*40, "\n2. CORRECTING DATA TYPES\n", "*"*40)

print("Process started: Converting date and categorical columns across all tables...")

# Define columns in the orders table that contain dates/timestamps
datetime_cols_orders = ['order_purchase_timestamp', 'order_approved_at', 'order_delivered_carrier_date', 'order_delivered_customer_date', 'order_estimated_delivery_date']
# Convert these string/object columns into actual pandas datetime objects. 
# errors='coerce' turns invalid parsing attempts into NaT (Not a Time).
for col in datetime_cols_orders:
    orders[col] = pd.to_datetime(orders[col], errors='coerce')
# Convert order status to a category data type to save memory and speed up processing
orders['order_status'] = orders['order_status'].astype('category')

# Convert shipping limit date to a datetime object
order_items['shipping_limit_date'] = pd.to_datetime(order_items['shipping_limit_date'], errors='coerce')
# Ensure price and freight values are numeric and downcast to float32
order_items[['price', 'freight_value']] = order_items[['price', 'freight_value']].apply(pd.to_numeric, errors='coerce').astype('float32')

# Define datetime columns for the reviews table and convert them
datetime_cols_reviews = ['review_creation_date', 'review_answer_timestamp']
for col in datetime_cols_reviews:
    reviews[col] = pd.to_datetime(reviews[col], errors='coerce')
# Convert review scores to integers. Using capitalized 'Int8' allows the column to hold NaN values if any exist.
reviews['review_score'] = pd.to_numeric(reviews['review_score'], errors='coerce').astype('Int8') 

# Ensure payment values are numeric and downcast to float32
payments['payment_value'] = pd.to_numeric(payments['payment_value'], errors='coerce').astype('float32')
# Convert payment installments to nullable integers ('Int8')
payments['payment_installments'] = pd.to_numeric(payments['payment_installments'], errors='coerce').astype('Int8')
# Convert payment types (e.g., credit card, boleto) to categorical data
payments['payment_type'] = payments['payment_type'].astype('category')

# Define all numeric measurement columns in the products table
product_numeric_cols = ['product_name_lenght', 'product_description_lenght', 'product_photos_qty', 'product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm']
# Loop through and enforce numeric data types on them
for col in product_numeric_cols:
    products[col] = pd.to_numeric(products[col], errors='coerce')

# FIX: Safely cast to string, remove any trailing ".0" if read as float, then pad with zeros
# Example: 1234.0 becomes '01234'. This is critical because zip codes are categorical strings, not math values.
customers['customer_zip_code_prefix'] = customers['customer_zip_code_prefix'].astype(str).str.replace(r'\.0$', '', regex=True).str.zfill(5)

print("Process complete: All data types standardized.\n")

# *****************************************************************************
# 3. CREATING NEW VARIABLES (FEATURE ENGINEERING)
# *****************************************************************************
print("*"*40, "\n3. CREATING NEW VARIABLES\n", "*"*40)

print("Process started: Engineering temporal features in 'orders'...")
# Extract the year, month, day name, and hour from the purchase timestamp
orders['purchase_year'] = orders['order_purchase_timestamp'].dt.year
orders['purchase_month'] = orders['order_purchase_timestamp'].dt.month
orders['purchase_day_of_week'] = orders['order_purchase_timestamp'].dt.day_name()
orders['purchase_hour'] = orders['order_purchase_timestamp'].dt.hour

# Create a binary flag (1 or 0) indicating if the purchase happened on a weekend using np.where
# DOWNCAST: Optimized to 8-bit integer to save memory
orders['is_weekend'] = np.where(orders['purchase_day_of_week'].isin(['Saturday', 'Sunday']), 1, 0).astype('int8')

# Calculate total delivery time in days
orders['delivery_time_days'] = (orders['order_delivered_customer_date'] - orders['order_purchase_timestamp']).dt.days
# Calculate how many days early or late the delivery was compared to the estimate
orders['delivery_delay_days'] = (orders['order_delivered_customer_date'] - orders['order_estimated_delivery_date']).dt.days

# Create a binary flag indicating if the delivery arrived after the estimated date
# DOWNCAST: Optimized to 8-bit integer to save memory
orders['is_late_delivery'] = np.where(orders['delivery_delay_days'] > 0, 1, 0).astype('int8')
print("Process complete: Order temporal features generated.\n")

print("Process started: Engineering volume features in 'products'...")
# Calculate the total physical volume of the product in cubic centimeters (L x W x H)
products['product_volume_cm3'] = products['product_length_cm'] * products['product_width_cm'] * products['product_height_cm']
print("Process complete: Product volume generated.\n")

print("Process started: Engineering pricing metrics in 'order_items'...")
# Calculate the full cost to the customer for an item (product price + shipping)
order_items['total_item_value'] = order_items['price'] + order_items['freight_value']

# DOWNCAST: Convert currency columns to 32-bit float to optimize memory footprint
order_items['price'] = order_items['price'].astype('float32')
order_items['freight_value'] = order_items['freight_value'].astype('float32')
order_items['total_item_value'] = order_items['total_item_value'].astype('float32')

# FIX: Use np.where to prevent ZeroDivisionError cleanly instead of using epsilon (1e-5)
# Calculate what percentage of the total cost went toward shipping (freight)
order_items['freight_ratio'] = np.where(
    order_items['total_item_value'] > 0, 
    order_items['freight_value'] / order_items['total_item_value'], 
    0
)
print("Process complete: Pricing metrics generated.\n")

print("Process started: Engineering review behaviors in 'reviews'...")
# Calculate how many days it took for a customer to respond to the review survey
reviews['review_response_time_days'] = (reviews['review_answer_timestamp'] - reviews['review_creation_date']).dt.days
# Create a binary flag indicating whether the user left a written comment (not just a star rating)
reviews['has_text_review'] = np.where(reviews['review_comment_message'].notnull(), 1, 0)
print("Process complete: Review features generated.\n")

# *****************************************************************************
# 4. DUPLICATE AND OUTLIERS REMOVAL
# *****************************************************************************
print("*"*40, "\n4. DUPLICATE AND OUTLIERS REMOVAL\n", "*"*40)

print("Process started: Removing duplicates across all tables...")
# Ensure each primary key or composite key is strictly unique to prevent double-counting in joins
customers.drop_duplicates(subset=['customer_id'], inplace=True)
orders.drop_duplicates(subset=['order_id'], inplace=True)
products.drop_duplicates(subset=['product_id'], inplace=True)
order_items.drop_duplicates(subset=['order_id', 'order_item_id'], inplace=True)
payments.drop_duplicates(subset=['order_id', 'payment_sequential'], inplace=True)
reviews.drop_duplicates(subset=['review_id', 'order_id'], inplace=True)
print("Process complete: Duplicates removed.\n")

print("Process started: Removing outliers and logical impossibilities...")
# Filter out illogical data: Delivery time cannot be negative
orders = orders[orders['delivery_time_days'] >= 0]
# Filter out free items (price <= 0), negative freight, or excessively high freight errors
order_items = order_items[(order_items['price'] > 0) & (order_items['freight_value'] >= 0) & (order_items['freight_value'] < 10000)]
# Ensure products have valid mass and dimensions
products = products[(products['product_weight_g'] > 0) & (products['product_volume_cm3'] > 0)]
# Ensure payments are positive and below a reasonable maximum threshold
payments = payments[(payments['payment_value'] > 0) & (payments['payment_value'] < 50000)]
# Ensure a review answer cannot pre-date the review creation
reviews = reviews[reviews['review_response_time_days'] >= 0]
print("Process complete: Outliers removed.\n")

# *****************************************************************************
# 5. DATA AGGREGATION AND MERGING
# *****************************************************************************
print("*"*40, "\n5. DATA AGGREGATION AND MERGING\n", "*"*40)

print("Process started: Aggregating payments by order...\n  Don't worry! This may take longer than expected.")
# Group by order_id because a single order can be paid with multiple payment methods or split cards
payments_agg = payments.groupby('order_id').agg({
    'payment_value': 'sum',                           # Sum up all partial payments
    'payment_installments': 'max',                    # Get the maximum number of installments used
    'payment_type': lambda x: ', '.join(x.dropna().astype(str).unique()) # Combine multiple payment types into one comma-separated string
}).reset_index()
# Rename the sum column for clarity
payments_agg.rename(columns={'payment_value': 'total_payment_value'}, inplace=True)
print("Process complete: Payments aggregated.\n")

print("Process started: Building the Master Analytical DataFrame...")
# Iteratively merge all tables into one flat master view using inner joins
# 1. Join orders with their respective customers
master_df = orders.merge(customers, on='customer_id', how='inner')
# 2. Add the aggregated payment data for each order
master_df = master_df.merge(payments_agg, on='order_id', how='inner')
# 3. Add the individual items purchased in each order
master_df = master_df.merge(order_items, on='order_id', how='inner')
# 4. Add the product catalog details for each item
master_df = master_df.merge(products, on='product_id', how='inner')

print("Process started: Adding review scores to Master DataFrame...")
# Aggregate review data per order (an order might have multiple items/reviews)
reviews_agg = reviews.groupby('order_id').agg({
    'review_score': 'mean',                   # Average review score for the order
    'has_text_review': 'max',                 # If at least one review had text, this becomes 1
    'review_response_time_days': 'mean'       # Average time taken to leave the review
}).reset_index()

# Left join the aggregated reviews because not every order will have a review attached
master_df = master_df.merge(reviews_agg, on='order_id', how='left')
print(f"Process complete: Master DataFrame created. Total rows for analysis: {len(master_df)}\n")

# *****************************************************************************
# 6. EXPORTING TABLES BACK TO MySQL
# *****************************************************************************
print("*"*40, "\n6. EXPORTING TABLES BACK TO MySQL\n", "*"*40)

# Dictionary bundling the cleaned and master dataframes for export
engineered_dfs = {
    "customers_cleaned": customers, 
    "orders_cleaned": orders,
    "products_cleaned": products,
    "order_items_cleaned": order_items,
    "payments_cleaned": payments,
    "reviews_cleaned": reviews,
    "master_analytical_view": master_df 
}

print("Process started: Sanitizing data types for MySQL compatibility...")
# Iterate over every dataframe and column to fix types that SQLAlchemy/MySQL struggle to interpret natively
for name, df in engineered_dfs.items():
    for col in df.columns:
        # Convert pandas Categorical types back to standard strings
        if isinstance(df[col].dtype, pd.CategoricalDtype):
            df[col] = df[col].astype(str)
        # Convert pandas nullable integer arrays ('Int8', 'Int64') to standard float64 arrays
        # (This is necessary because MySQL needs standard numeric types to handle the embedded NaNs safely)
        elif pd.api.types.is_extension_array_dtype(df[col].dtype) and 'Int' in str(df[col].dtype):
            df[col] = df[col].astype('float64')
print("Process complete: Data types sanitized.\n")

print("Process started: Exporting cleaned tables to database...\n  Don't worry! This may take longer than expected.")
# Write each dataframe back to the MySQL database
for table_name, df in engineered_dfs.items():
    print(f"  -> Exporting '{table_name}'...")
    # if_exists='replace' overwrites the table if it already exists.
    # chunksize=10000 ensures memory efficiency by sending inserts in batches of 10,000 rows.
    df.to_sql(name=table_name, con=engine, if_exists='replace', index=False, chunksize=10000)
print("Process complete: All data exported successfully.\n")

# Safely close the SQLAlchemy connection pool
engine.dispose()
print("FINAL PROCESS: Database connection engine disposed. Pipeline complete.")

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