-- ===================================================================================
-- Stage 2: MySQL Database Creation & Data Ingestion
-- ===================================================================================
-- Description: This script sets up the local MySQL environment for the e-commerce 
-- analytics project. It drops any existing database to ensure a clean slate, defines 
-- the schema for 6 core tables, and bulk-loads the raw CSV data into them.
-- ===================================================================================

-- ===================================================================================
-- 1. CLEAN SLATE AND CREATE DATABASE
-- ===================================================================================
-- First things first: let's make sure we're starting fresh. 
-- Dropping the database if it already exists prevents duplicate data or schema 
-- conflicts if we ever need to re-run this script from scratch.
DROP DATABASE IF EXISTS ecomm_analytics;

-- Now, create our new database and tell MySQL to use it for all subsequent operations.
CREATE DATABASE ecomm_analytics;
USE ecomm_analytics;

-- ===================================================================================
-- 2. CREATE TABLES
-- ===================================================================================
-- Setting up the schema. I'm using "IF NOT EXISTS" as a standard best practice 
-- safety net, even though we just dropped the DB above.

-- Customers Table
-- Holds basic geographic and demographic info for the buyers.
-- customer_id is the primary key used to link to the orders table.
CREATE TABLE IF NOT EXISTS customers (
    customer_id VARCHAR(50) PRIMARY KEY,
    customer_unique_id VARCHAR(50),      -- A unique ID for the user (since a user can have multiple customer_ids per order)
    customer_zip_code_prefix INT,        -- Storing zip as INT to save space and optimize indexing
    customer_city VARCHAR(50),
    customer_state CHAR(2)               -- Using CHAR(2) since states are represented by their 2-letter codes
);

-- Orders Table
-- The central hub of our dataset. Every transaction goes through here.
CREATE TABLE IF NOT EXISTS orders (
    order_id VARCHAR(50) PRIMARY KEY,
    customer_id VARCHAR(50),             -- Foreign key reference to customers table
    order_status VARCHAR(20),            -- e.g., 'delivered', 'shipped', 'canceled'
    order_purchase_timestamp DATETIME,
    order_approved_at DATETIME,
    order_delivered_carrier_date DATETIME,
    order_delivered_customer_date DATETIME,
    order_estimated_delivery_date DATETIME
);

-- Products Table
-- Details about the physical items being sold. 
-- Note: Sticking to the original source data spelling for "lenght" to avoid mismatch errors later.
CREATE TABLE IF NOT EXISTS products (
    product_id VARCHAR(50) PRIMARY KEY,
    product_category_name VARCHAR(50),
    product_name_lenght INT,             -- Kept typo 'lenght' from original dataset
    product_description_lenght INT,      -- Kept typo 'lenght' from original dataset
    product_photos_qty INT,
    product_weight_g INT,                -- Weight in grams
    product_length_cm INT,
    product_height_cm INT,
    product_width_cm INT
);

-- Order Items Table
-- A bridge table breaking down individual items within a single order.
-- One order_id can have multiple rows here if the customer bought multiple products.
CREATE TABLE IF NOT EXISTS order_items (
    order_id VARCHAR(50),
    order_item_id INT,                   -- Sequential number identifying the number of items included in the same order
    product_id VARCHAR(50),
    seller_id VARCHAR(50),
    shipping_limit_date DATETIME,
    price DECIMAL(10, 2),                -- Standard decimal format for currency (10 digits total, 2 after decimal)
    freight_value DECIMAL(10, 2)         -- Shipping cost
);

-- Payments Table
-- Tracks how the customer paid. Multiple payment methods can be used for a single order.
CREATE TABLE IF NOT EXISTS payments (
    order_id VARCHAR(50),
    payment_sequential INT,              -- In case a customer splits payment (e.g., 2 different credit cards)
    payment_type VARCHAR(20),            -- e.g., 'credit_card', 'boleto', 'voucher'
    payment_installments INT,            -- Number of installments chosen by the customer
    payment_value DECIMAL(10, 2)
);

-- Reviews Table
-- Customer feedback data. This one can be tricky to import because users often press 'Enter' 
-- inside the review_comment_message, creating multi-line strings.
CREATE TABLE IF NOT EXISTS reviews (
    review_id VARCHAR(50),
    order_id VARCHAR(50),
    review_score INT,                    -- Usually 1 to 5
    review_comment_title VARCHAR(255),
    review_comment_message TEXT,         -- TEXT datatype used here since reviews can get pretty long
    review_creation_date DATETIME,
    review_answer_timestamp DATETIME
);

-- ===================================================================================
-- 3. LOAD DATA INFILE COMMANDS
-- ===================================================================================
-- We're using LOAD DATA INFILE because it's significantly faster for bulk imports 
-- compared to standard INSERT statements. 

-- Load Customers (Reverted to \n)
-- NOTE: The file path below is specific to my local Windows environment. 
-- If you are running this script, please replace the path below with your local MySQL 'Uploads' directory path.
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/olist_customers_dataset.csv'
INTO TABLE customers
FIELDS TERMINATED BY ','                 -- Standard CSV comma separation
ENCLOSED BY '"'                          -- Handles commas that might be inside the actual data strings
LINES TERMINATED BY '\n'                 -- Expecting Unix-style line breaks based on how the CSV was saved
IGNORE 1 ROWS;                           -- Skip the header row so we don't import column names as data

-- Load Orders (Reverted to \n)
-- For the Orders table, we have a bunch of datetime columns. If the CSV has empty strings ('') 
-- for dates (like when an order hasn't been delivered yet), MySQL's strict mode will throw an error. 
-- To fix this, we load those columns into temporary user variables (e.g., @v_purchase) 
-- and use NULLIF to cleanly convert those empty strings into proper SQL NULL values.
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/olist_orders_dataset.csv'
INTO TABLE orders
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(order_id, customer_id, order_status, @v_purchase, @v_approved, @v_carrier, @v_delivered, @v_estimated)
SET 
order_purchase_timestamp = NULLIF(@v_purchase, ''),
order_approved_at = NULLIF(@v_approved, ''),
order_delivered_carrier_date = NULLIF(@v_carrier, ''),
order_delivered_customer_date = NULLIF(@v_delivered, ''),
order_estimated_delivery_date = NULLIF(@v_estimated, '');

-- Load Products (Reverted to \n)
-- Applying the same NULLIF logic here. If a product is missing its dimensions or weight in the CSV, 
-- we want to store it as a proper NULL rather than crashing the import process or storing a blank string in an INT column.
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/olist_products_dataset.csv'
INTO TABLE products
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(product_id, product_category_name, @v_name_len, @v_desc_len, @v_photos_qty, @v_weight, @v_length, @v_height, @v_width)
SET 
product_name_lenght = NULLIF(@v_name_len, ''),
product_description_lenght = NULLIF(@v_desc_len, ''),
product_photos_qty = NULLIF(@v_photos_qty, ''),
product_weight_g = NULLIF(@v_weight, ''),
product_length_cm = NULLIF(@v_length, ''),
product_height_cm = NULLIF(@v_height, ''),
product_width_cm = NULLIF(@v_width, '');

-- Load Order Items (Reverted to \n)
-- This is a straightforward import since there are no tricky empty dates to handle.
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/olist_order_items_dataset.csv'
INTO TABLE order_items
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Load Payments (Reverted to \n)
-- Another straightforward import.
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/olist_order_payments_dataset.csv'
INTO TABLE payments
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Load Reviews
-- Reviews are always the wildcard. Because users type these out, the text often contains 
-- weird characters, embedded commas, and random line breaks (carriage returns).
-- We use ESCAPED BY '"' to handle internal quotes, and specifically look for Windows-style 
-- '\r\n' line terminators to make sure we don't accidentally split a single review across multiple rows.
-- We also apply the NULLIF trick for the timestamp columns just in case they are empty.
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/olist_order_reviews_dataset.csv'
INTO TABLE reviews
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
ESCAPED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS
(review_id, order_id, review_score, review_comment_title, review_comment_message, @v_creation, @v_answer)
SET 
review_creation_date = NULLIF(@v_creation, ''),
review_answer_timestamp = NULLIF(@v_answer, '');


/*
=============================================================================
👨‍💻 Author: Animesh Sanghi
=============================================================================
Title:    Data Analyst | MBA '28 (Analytics & Data Science) MUJ
Phone:    9406570600
Email:    animeshsanghi.da@gmail.com
LinkedIn: https://www.linkedin.com/in/animeshsanghi-da/
GitHub:   https://github.com/animeshsanghi-da
=============================================================================
*/