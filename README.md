# Olist E-Commerce Data Analysis 📊 

---

**Date of Completion:** April 1, 2026

[![Olist Dataset](https://img.shields.io/badge/Olist-Dataset-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)  [![GitHub](https://img.shields.io/badge/GitHub-Repository-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/animeshsanghi-da)  [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/animeshsanghi-da/)

[![Windows](https://img.shields.io/badge/Windows-Supported-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://www.microsoft.com/windows)  [![Linux](https://img.shields.io/badge/Linux-Supported-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://www.linux.org/)  [![macOS](https://img.shields.io/badge/macOS-Supported-000000?style=for-the-badge&logo=apple&logoColor=white)](https://www.apple.com/macos/)

[![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://www.mysql.com/)  [![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)  [![VS Code](https://img.shields.io/badge/VS_Code-Editor-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)](https://code.visualstudio.com/) [![Anaconda](https://img.shields.io/badge/Anaconda-Environment-44A833?style=for-the-badge&logo=anaconda&logoColor=white)](https://www.anaconda.com/)

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)  [![Pandas](https://img.shields.io/badge/Pandas-Data_Cleaning-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)  [![NumPy](https://img.shields.io/badge/Numpy-Data_Math-777BB4?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/) [![Scikit-Learn](https://img.shields.io/badge/scikit_learn-Machine_Learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/) [![python-dotenv](https://img.shields.io/badge/python--dotenv-Config-ECD53F?style=for-the-badge&logo=python&logoColor=white)](https://github.com/theskumar/python-dotenv) [![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/) [![MySQL Connector](https://img.shields.io/badge/MySQL_Connector-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white)](https://dev.mysql.com/doc/connector-python/en/) [![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualisation-11557C?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org/) [![Seaborn](https://img.shields.io/badge/Seaborn-Statistical_Plots-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)

[![Animesh Sanghi](https://img.shields.io/badge/ANIMESH%20SANGHI-DATA%20ANALYST-0A66C2?style=for-the-badge&logo=codeforces&logoColor=white)](Animesh_Resume.pdf) [![Gmail](https://img.shields.io/badge/Gmail-animeshsanghi.da@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:animeshsanghi.da@gmail.com) [![WhatsApp](https://img.shields.io/badge/WhatsApp-%2B91_9406570600-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/919406570600)

---

*[Olist website](https://olist.com/) view for product listing:* ![Dashboard Preview](Example_of_a_product_listing.png)

<br>

## 📌 Project Overview

---

This project involves a detailed analysis of a Brazilian E-commerce dataset provided by Olist on Kaggle. The dataset contains multiple tables with over 100k rows of data showing customer behavior, logistics, sales, and product performance. 

**About the Data:** This dataset has over 2 million views and 487K downloads as of April 1, 2026.
It contains information on 100k orders made across multiple marketplaces in Brazil from 2016 to 2018.  
This is real, anonymized commercial data. Company and partner names in the reviews have been replaced with Game of Thrones house names.  
**Note:** Column names such as `product_name_lenght` and `product_description_lenght` keep their original spelling from the source database to ensure our data pipeline works correctly.

**Acknowledgements:**  
Thanks to [Olist](https://olist.com/) for releasing this dataset.  
Thanks to [Kaggle](https://www.kaggle.com/) for making it available.  

**Approach:**
To keep things structured and professional, this project follows the industry-standard 6-stage data analytics framework: **Ask, Prepare, Process, Analyse, Share, and Act.**

**Project Report:**
You can also explore the entire process without installing any applications by reading the [Olist_Project_Report.pdf](Olist_Project_Report.pdf). This report is a complete compilation of all scripts and their outputs, and reviewing it requires no technical setup.

**Executive Summary & Business Impact:**  
👉 View the final presentation: **[Markdown Version](6.1_Stage_6-ACT_Presentation.md)** | **[PDF Slides](6.1_Stage_6-ACT_Presentation.pdf)**  
Key Insights:
* **Late Deliveries Hurt Reviews:** When an order arrives late, customer ratings drop by ~40% (falling from about 4.2 to 2.5 stars). Every extra day of delay lowers the score by another 0.05 stars.
* **Peak Shopping Times:** Most sales happen early in the workweek, specifically Mondays and Tuesdays between 1:00 PM and 4:00 PM. The absolute busiest time is Monday at 4:00 PM, with most people paying by credit card.
* **High Shipping Costs Cause Cancellations:** Expensive delivery fees turn buyers away. If shipping makes up more than 20% of the total order cost, cancellations go up. If it crosses 33%, it hits a "danger zone" where customers are highly likely to cancel their orders.

<br>

## 🚀 TL;DR: Key Business Impact

---

* **Revenue Optimisation:** Proved a 0.32 correlation between payment installments and higher checkout values, guiding new ad spend strategies.
* **Logistics ROI:** Built a Linear Regression model proving that every 1 day of shipping delay mathematically destroys average review scores by ~0.05 stars.
* **Catalog Efficiency:** Disproved the company myth that massive product descriptions improve customer satisfaction.

<br>

## 🛠️ Prerequisites & Software Requirements

---

This project was developed on **Windows 10 (64-bit)** using **VS Code**, **Anaconda**, **Jupyter Lab**, and **MySQL**. To run the analysis on your local machine, make sure you have these applications (or their alternatives) installed on your operating system (Windows, Linux, or macOS).

**The Tech Stack:**
* **Database:** MySQL (for local data storage and extraction)
* **Language:** Python 3.10+
* **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, SQLAlchemy, Scikit-learn, mysql-connector-python, and python-dotenv.

**Required Software and Alternatives:**
* **MySQL Community Server:** Essential for hosting the local e-commerce database.  
*(Alternatives: MariaDB as an open-source replacement, or running MySQL via Docker Desktop).*
* **Anaconda (or Miniconda):** Essential for recreating the isolated Python environment and installing the exact dependencies without system conflicts.  
*(Alternative: Standard Python 3.10+ using venv and pip).*

**Recommended Tools and Alternatives:**
* **MySQL Workbench:** Highly recommended for running the initial SQL scripts and checking the tables visually.  
*(Alternatives: DBeaver or JetBrains DataGrip. These are great if MySQL Workbench runs poorly on your Linux or macOS setup).*
* **Jupyter Lab or Jupyter Notebook:** Recommended for opening and running the .ipynb analysis and visualisation files.  
*(Alternatives: The VS Code Jupyter Extension, or Google Colab to run notebooks in the cloud).*
* **Visual Studio Code:** A great all-in-one editor for viewing the Python scripts (.py), Markdown files (.md), and SQL queries.  
*(Alternatives: PyCharm or Sublime Text).*

<br>

## 🔐 Environment Setup (Database Password)

---

This project connects to a local MySQL database. To avoid typing your password manually every time a script runs, you should set up an environment file:
1. Find the [.env.example](.env.example) file in the main folder.
2. Duplicate it and rename the copy to exactly [.env](.env).
3. Open the [.env](.env) file and replace `your_mysql_password_here` with your actual MySQL password.

**Smart Fallback Feature:** If you choose not to use a [.env](.env) file, or if the password inside it is wrong, the scripts will not crash. Instead, the system will politely ask you to enter the password manually in the terminal (you get a maximum of 3 attempts).

<br>

## 🌍 Environment Setup (Anaconda)

---

Data science projects need specific versions of libraries (like pandas, scikit-learn, and seaborn). Relying on your computer's default Python can cause version conflicts.
This project uses Anaconda to create a strictly isolated environment. This ensures anyone can run the code smoothly without breaking their local setup.

<br>

## 📂 Project Structure

---

The repository contains around 50 files. It is organised chronologically to follow the 6 stages of data analytics:

### Project & Analyst Overview
* **[Olist_Project_Report.pdf](Olist_Project_Report.pdf)** - Comprehensive compilation of all project scripts, methodologies, and outputs. *(Primary Deliverable)*
* **[Animesh_Resume.pdf](Animesh_Resume.pdf)** - Author's detailed Data Analyst resume.

### Documentation & Environment Setup
* **[README.md](README.md)** OR **[.pdf](README.pdf)** - Complete project guide, architecture overview, and execution instructions. *(Start Here)*
* [0.1_env_setup_guide.md](0.1_env_setup_guide.md) OR [.pdf](0.1_env_setup_guide.pdf) - Step-by-step instructions for Python environment and dependency configuration.
* [requirements.txt](requirements.txt) - Required Python libraries and dependencies for isolated environment setup.
* [.env.example](.env.example) - Template for environment variables; requires local configuration for database credentials.
* [.gitignore](.gitignore) - Configuration file for secure GitHub version control.

### Stage 1: Ask (Problem Definition)
* **[1.0_Stage_1-ASK-Business_Questions.md](1.0_Stage_1-ASK-Business_Questions.md)** OR **[.pdf](1.0_Stage_1-ASK-Business_Questions.pdf)** - Core business problems, stakeholder questions, and defined analytical objectives. *(Core Document)*

### Stage 2: Prepare (Database Setup)
* **[2.1_Stage_2-PREPARE-Database_Setup.sql](2.1_Stage_2-PREPARE-Database_Setup.sql)** OR **[.pdf](2.1_Stage_2-PREPARE-Database_Setup.pdf)** - SQL scripts for building the database schema and ingesting raw dataset files. *(Core Script)*

### Stage 3: Process (Data Cleaning & Pipeline)
* **[utils.py](utils.py)** - Custom utility scripts for establishing secure MySQL database connections. *(Core Script)*
* **[3.1_Stage_3-PROCESS_Diagnosis_Raw.py](3.1_Stage_3-PROCESS_Diagnosis_Raw.py)** - Python script for initial raw data diagnostics and exploration. *(Core Script)*
* [3.2_Stage_3-PROCESS_Diagnosis_Raw_Output.txt](3.2_Stage_3-PROCESS_Diagnosis_Raw_Output.txt) - Terminal execution log documenting the raw data diagnosis.
* **[3.3_Stage_3-PROCESS_Cleaning_Data.py](3.3_Stage_3-PROCESS_Cleaning_Data.py)** - Automated Python pipeline for data cleaning, type conversion, and formatting. *(Core Script)*
* [3.4_Stage_3-PROCESS_Cleaning_Data_Output.txt](3.4_Stage_3-PROCESS_Cleaning_Data_Output.txt) - Terminal execution log for the cleaning pipeline.
* **[3.5_Stage_3-PROCESS_Diagnosis_Cleaned.py](3.5_Stage_3-PROCESS_Diagnosis_Cleaned.py)** - Python script to validate and diagnose the cleaned dataset. *(Core Script)*
* [3.6_Stage_3-PROCESS_Diagnosis_Cleaned_output.txt](3.6_Stage_3-PROCESS_Diagnosis_Cleaned_output.txt) - Terminal execution log for post-cleaning validation.

### Stage 4: Analyze (EDA & Modeling)
* **[4.0_Stage_4-ANALYSE_Analysis.ipynb](4.0_Stage_4-ANALYSE_Analysis.ipynb)** OR **[.pdf](4.0_Stage_4-ANALYSE_Analysis.pdf)** - Jupyter Notebook detailing Exploratory Data Analysis (EDA) and predictive machine learning models. *(Primary Deliverable)*

### Stage 5: Share (Data Visualization)
* **[5.0_Stage_5-SHARE_Visualisation_Report.ipynb](5.0_Stage_5-SHARE_Visualisation_Report.ipynb)** OR **[.pdf](5.0_Stage_5-SHARE_Visualisation_Report.pdf)** - Technical notebook documenting the generation of data visualizations and business dashboards. *(Technical Overview)*
* **[5.1_Stage_5-SHARE_Presentation.md](5.1_Stage_5-SHARE_Presentation.md)** OR **[.pdf](5.1_Stage_5-SHARE_Presentation.pdf)** - Slide deck outlining the visual insights derived from the data. *(Stakeholder Presentation)*

### Stage 6: Act (Business Strategy & Conclusion)
* **[6.0_Stage_6-ACT_Executive_Summary_Report.md](6.0_Stage_6-ACT_Executive_Summary_Report.md)** OR **[.pdf](6.0_Stage_6-ACT_Executive_Summary_Report.pdf)** - Comprehensive written report detailing final business insights and strategic recommendations. *(Technical Overview)*
* **[6.1_Stage_6-ACT_Presentation.md](6.1_Stage_6-ACT_Presentation.md)** OR **[.pdf](6.1_Stage_6-ACT_Presentation.pdf)** - Executive slide deck directly connecting data visualizations to actionable business growth strategies. *(Stakeholder Presentation)*

<br>

## 🚀 How to Run the Project (Start to Finish)

---

Follow these steps to run the project locally from scratch:

> ***Note:*** *Please don't confuse "steps" and "stages" as they mean different things in this project.*

*[Download the dataset from Kaggle:](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)* ![Kaggle Preview](olist_on_kaggle.png)

### Step 1: Clone the Repository
1. **Clone the Repository**: Download or clone this project from GitHub to your local machine.
2. **Prepare the Data**: Inside the main project folder, create a new folder named data. Extract and save all the CSV files downloaded from Kaggle into this data folder.
3. **Launch Terminal**: Open the main project folder in your terminal or command prompt.
Example *(replace the path with your actual folder path)*:
```bash
cd C:\Users\MY PC\Downloads\Olist_project_by_animesh
```

### Step 2: Setup the Python Environment
This project uses an Anaconda environment to prevent library conflicts. In your terminal, run these commands one by one:
```bash
conda create --name animesh_env --file requirements.txt
```
```bash
conda activate animesh_env
```
```bash
python -m ipykernel install --user --name=animesh_env --display-name="Python (E-commerce Project)"
```
>*Check the [0.1_env_setup_guide.md](0.1_env_setup_guide.md) or [.pdf](0.1_env_setup_guide.pdf) file for more details.*

### Step 3: Configure Database Credentials
Set up your [.env](.env) file as instructed in the Environment Setup section above so the Python scripts can safely access your local database.

### Step 4: Setup the Database (MySQL)
Open MySQL Workbench (or your preferred SQL client).  
>*Open and run the [2.1_Stage_2-PREPARE-Database_Setup.sql](2.1_Stage_2-PREPARE-Database_Setup.sql) file.*

This creates the `ecomm_analytics` database, builds the tables, and loads the raw CSV files into your local server.

### Step 5: Run the Data Pipeline (Processing & Cleaning)
>Activate `animesh_env` and run these Python scripts in your terminal (or an editor like VSCode) or preferred app to [diagnose](3.1_Stage_3-PROCESS_Diagnosis_Raw.py), [clean](3.3_Stage_3-PROCESS_Cleaning_Data.py), and [prepare](3.5_Stage_3-PROCESS_Diagnosis_Cleaned.py) the data:
1.  ```bash
    python 3.1_Stage_3-PROCESS_Diagnosis_Raw.py
    ```
2.  ```bash
    python 3.3_Stage_3-PROCESS_Cleaning_Data.py
    ```
3.  ```bash
    python 3.5_Stage_3-PROCESS_Diagnosis_Cleaned.py
    ```

### Step 6: Explore the Analysis & Visualisations

Open Jupyter Lab (or your preferred app) and make sure your kernel is set to `Python (E-commerce Project)`. Then, open and run all cells in these notebooks:

1. [4.0_Stage_4-ANALYSE_Analysis.ipynb](4.0_Stage_4-ANALYSE_Analysis.ipynb) – to view the EDA and predictive model.
2. [5.0_Stage_5-SHARE_Visualisation_Report.ipynb](5.0_Stage_5-SHARE_Visualisation_Report.ipynb) – to generate business charts (this also saves them as PNGs).

>*Just want to see the results? Check out the PDFs: [analyse](4.0_Stage_4-ANALYSE_Analysis.pdf) and [share](5.0_Stage_5-SHARE_Visualisation_Report.pdf).*

### Step 7: Explore the Presentations and Act Report
Open VS Code (or your preferred app) to review the final presentations and reports:

1. **[5.1_Stage_5-SHARE_Presentation.md](5.1_Stage_5-SHARE_Presentation.md)**: A presentation showing the key visual insights for stakeholders.
2. **[6.0_Stage_6-ACT_Executive_Summary_Report.md](6.0_Stage_6-ACT_Executive_Summary_Report.md)**: A written report on the best steps for business growth.
3. **[6.1_Stage_6-ACT_Presentation.md](6.1_Stage_6-ACT_Presentation.md)**: A presentation connecting the data visuals directly to business strategies.

>*Just want a quick look? Check out the PDFs: [stage-5 presentation](5.1_Stage_5-SHARE_Presentation.pdf), [stage-6 report](6.0_Stage_6-ACT_Executive_Summary_Report.pdf), and [stage-6 presentation](6.1_Stage_6-ACT_Presentation.pdf).*

<br>

## 🎯 Stage 1: Ask (Defining the Business Problem)

---

**The Business Objective:** To find actionable insights regarding sales trends, shipping delays, customer buying behavior, and catalog optimisation to drive revenue, improve delivery times, and keep customers coming back.

**Key Analytical Focus Areas:**
1. **Sales & Revenue Trends:** Analysing Month-over-Month (MoM) growth, peak traffic times (day/hour), and Average Order Value (AOV).
2. **Logistics & Operational Efficiency:** Checking average delivery times and finding out which regions are the slowest.
3. **Customer Behavior & Segmentation:** Understanding how people pay and checking if payment installments lead to bigger orders.
4. **Product Catalog & Satisfaction:** Comparing sales volume vs. revenue across categories and testing if longer descriptions or more photos actually improve review scores.
5. **Predictive Impact Analysis:** Using Linear Regression to mathematically calculate the "Late Penalty"—meaning exactly how much a review score drops for every extra day a delivery is late.

>*Note: All core business questions from stakeholders and the specific analytical questions addressed in this project are listed in the [1.0_Stage_1-ASK-Business_Questions.md](1.0_Stage_1-ASK-Business_Questions.md) or [.pdf](1.0_Stage_1-ASK-Business_Questions.pdf) file.*

<br>

## 🛠️ Stage 2: Prepare (Setting Up & Gathering Data)

---

The raw data comes from the [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce). Raw CSV files were successfully loaded into a **MySQL database** for safe storage and easy querying.

*(MySQL Workbench view after loading all files)* ![Dashboard Preview](MySQL.png)

**Core Tables Used:**
| | Table Name | Description | Key Columns |
| :--- | :--- | :--- | :--- |
|1.| **[Orders](data/olist_orders_dataset.csv)** | Core transaction data. | `order_id`, `customer_id`, `timestamp` |
|2.| **[Order_Items](data/olist_order_items_dataset.csv)** | Specific items per order. | `order_id`, `product_id`, `price` |
|3.| **[Products](data/olist_products_dataset.csv)** | Product catalog details. | `product_id`, `category_name` |
|4.| **[Customers](data/olist_customers_dataset.csv)** | Buyer demographics. | `customer_id`, `zip_code`, `city` |
|5.| **[Reviews](data/olist_order_reviews_dataset.csv)** | Customer feedback. | `review_score`, `review_comment` |
|6.| **[Payments](data/olist_order_payments_dataset.csv)** | Payment methods used. | `payment_type`, `payment_value` |

### Database Setup:
1. Created a centralized relational database in [MySQL Workbench](https://www.mysql.com/products/workbench/).
2. Set up the right schema and tables for the raw files.
3. Loaded the data using the `INFILE` command.

>*Note: The SQL queries for creating the database and loading data are in the [2.1_Stage_2-PREPARE-Database_Setup.sql](2.1_Stage_2-PREPARE-Database_Setup.sql) file.*

<br>

## 🧹 Stage 3: Process (Cleaning the Data)

---

Data cleaning was done using [Python](https://www.python.org/) ([Pandas](https://pandas.pydata.org/) & [NumPy](https://numpy.org/)) connected straight to the MySQL database. Python was chosen over pure [SQL](https://en.wikipedia.org/wiki/SQL) for this step because its libraries make complex changes and outlier handling much easier.

*(Schema of column names in the dataset tables)* ![Dashboard Preview](Data_Schema.png)

### Security First: Secure MySQL Password Handling in Python:

**Database Security: [utils.py](utils.py), [getpass](https://docs.python.org/3/library/getpass.html), & [load_dotenv](https://pypi.org/project/python-dotenv/)**

* **Why it was created:** Hardcoding database passwords is a major security risk, especially when sharing code in a [public GitHub repo](https://github.com/topics/public-repository).
* **The Setup:** I created a standalone script ([utils.py](utils.py)) using the [sqlalchemy](https://www.sqlalchemy.org/), [getpass](https://docs.python.org/3/library/getpass.html), [logging](https://docs.python.org/3/library/logging.html), [load_dotenv](https://pypi.org/project/python-dotenv/), and [os](https://docs.python.org/3/library/os.html) libraries.

**How it Works:**
The script securely handles your MySQL password using a two-step logic:
1.  **Automated:** It first tries to read the password from a [.env](.env) file (following the `Environment Setup` steps). In this process, [load_dotenv](https://pypi.org/project/python-dotenv/) loads the file, [os](https://docs.python.org/3/library/os.html) checks for its existence to extract the password, and then [sqlalchemy](https://www.sqlalchemy.org/) uses that password to establish the connection.
2.  **Manual Fallback:** If the [.env](.env) file is missing or has the wrong password, the [getpass](https://docs.python.org/3/library/getpass.html) library creates a hidden prompt in the terminal for manual entry.

**Attempt Logic:**
You have a total of **3 attempts** to enter the correct password:
* If a [.env](.env) file exists but contains the wrong password, it counts as an attempt.
* If the [.env](.env) file does not exist, it does not count as an attempt, and you proceed to manual entry.
**How to Use it:**
Instead of typing passwords into analysis files, simply import the connection function at the top of your notebooks:
```python
from utils import get_db_connection
engine = get_db_connection()
```

**Staying Safe on GitHub:**
To keep personal credentials off the web, the password stays in the .env file. I created a .gitignore file to ensure this file is automatically excluded during a git push.  
Note: .gitignore only works for command-line pushes; if you upload files manually to GitHub, ensure you do not include the .env file.

### The 6-Step Cleaning Workflow:

1. **Data Loading & Initial Cleaning:** Pulled all 6 tables from MySQL and formatted them for processing.
2. **Correcting Data Types & Optimisation:** 
    * Fixed dates and times to ensure time-series analysis works correctly.
    * Converted specific numeric columns using **`.astype('float32')`**.
    * **Why?** This significantly reduces memory usage. Switching from the default 64-bit to 32-bit keeps the notebook lightweight and improves processing speed, which is essential when handling large datasets.
3. **Feature Engineering:** Created new, helpful columns to enable deeper business analysis.
4. **Duplicate & Outlier Removal:** Cleaned up repeating data and extreme values to keep the statistical math accurate.
5. **Data Aggregation & Merging:** Combined all individual clean tables into one central `master_analytical_view`.
6. **Exporting to MySQL:** Sent the cleaned tables and the new master view back to the database. This keeps the original raw data safe while providing a "single source of truth" for the analysis phase.

>*Use these scripts depending on what you want to check:*

| Task | Script File & Expected Output |
| :--- | :--- |
| **Diagnosis of Raw Data** | [3.1_Stage_3-PROCESS_Diagnosis_Raw.py](3.1_Stage_3-PROCESS_Diagnosis_Raw.py) & [Expected Output](3.2_Stage_3-PROCESS_Diagnosis_Raw_Output.txt) |
| **Cleaning** | [3.3_Stage_3-PROCESS_Cleaning_Data.py](3.3_Stage_3-PROCESS_Cleaning_Data.py) & [Expected Output](3.4_Stage_3-PROCESS_Cleaning_Data_Output.txt) |
| **Diagnosis of Cleaned Data** | [3.5_Stage_3-PROCESS_Diagnosis_Cleaned.py](3.5_Stage_3-PROCESS_Diagnosis_Cleaned.py) & [Expected Output](3.6_Stage_3-PROCESS_Diagnosis_Cleaned_Output.txt) |

*(VS Code view while cleaning the data)* ![Dashboard Preview](vs_code_view_while_cleaning.png)

<br>

## 🔍 Stage 4: Analyse (Finding the Patterns)

---

In this step, the cleaned `master_analytical_view` was loaded into Jupyter Lab. Using Pandas, the data was thoroughly analysed to answer the business questions set in Stage 1.

Exploratory Data Analysis (EDA) was done to find links between payment installments and cart sizes, calculate the exact percentage of late deliveries, and find the best-selling product categories.

**Predictive Modeling:** [Scikit-learn](http://scikit-learn.org/) was used to build a Linear Regression model. This helped mathematically figure out the "Late Penalty" to predict exactly how much review scores drop when deliveries are late.

>*The full analysis and model training can be found in the [4.0_Stage_4-ANALYSE_Analysis.ipynb](4.0_Stage_4-ANALYSE_Analysis.ipynb) file.*

*(Jupyter Lab view while Analysing the data)* ![Dashboard Preview](jupyter_lab_analysing.png)

<br>

## 📈 Stage 5: Share (Visualising the Insights)

---

Numbers alone are hard to read. To turn backend data into front-end business value, the main findings were graphed using Matplotlib and Seaborn.

This stage includes 10+ clear, easy-to-read charts that show traffic peaks, delivery slowdowns, category earnings, and just how badly shipping delays hurt customer satisfaction.

>*The code used to generate the charts and the visualisations themselves can be found in the [5.0_Stage_5-SHARE_Visualisation_Report.ipynb](5.0_Stage_5-SHARE_Visualisation_Report.ipynb) file.*

>*I have also prepared a [5.1_Stage_5-SHARE_Presentation.md](5.1_Stage_5-SHARE_Presentation.md) file designed specifically for stakeholder meetings.*

>*Both the [report](5.0_Stage_5-SHARE_Visualisation_Report.pdf) and [presentation](5.1_Stage_5-SHARE_Presentation.pdf) are available in PDF format.*

*(Example: Peak Traffic Heatmap)* ![Dashboard Preview](VIZ-1.2-HEATMAP-Order_Volume.png)

<br>

## 💡 Stage 6: Act (Business Recommendations)

---

Based on the data, here are the strategic recommendations to help the business grow and fix operational issues:

1. **Strategic Timing & Payments:** Move ad spending to weekday afternoons (when traffic is highest) and strongly promote payment installment plans, which are proven to lead to bigger orders.
2. **Fix the "Late Penalty":** Do a full check on the shipping partners handling the Northern/Northeastern states. Our math shows that every extra day of delay costs the business ~0.05 stars, dropping average reviews from 4.29 to 2.27 and ruining trust.
3. **Optimise the Catalog:** Focus on keeping fast-selling items (like Health/Beauty and Bed/Bath) in stock. Stop spending time writing super long product descriptions, as the data shows they don't actually improve review scores.
4. **Launch a VIP Program:** Create a loyalty program with faster shipping for the top 5% of spenders who live in Rio de Janeiro, São Paulo, and Vitória.
5. **Implement a Retention Strategy:** Shift focus from just getting new customers to keeping the ones we have. Over 90% of buyers only ordered once; we need automated post-purchase discounts to get them to buy again.
6. **Deploy AI Operations:** Build an AI system using smart chatbots to handle basic customer support and active order tracking. This will cut down on staff costs and solve customer problems before they leave a 1-star review.

>*Read the full business strategy in the [6.0_Stage_6-ACT_Executive_Summary_Report.md](6.0_Stage_6-ACT_Executive_Summary_Report.md) file.*

>*I have also prepared a [6.1_Stage_6-ACT_Presentation.md](6.1_Stage_6-ACT_Presentation.md) file designed specifically for stakeholder meetings.*

>*Both the [report](6.0_Stage_6-ACT_Executive_Summary_Report.pdf) and [presentation](6.1_Stage_6-ACT_Presentation.pdf) are available in PDF format.*

*(PDF view of the ACT presentation)* ![Dashboard Preview](presentation_as_pdf.png)

<br>

## 🏁 Conclusion

---

This project was a great chance to use the full 6-stage data analytics framework on a massive, real-world e-commerce dataset. By taking the data all the way from raw CSV files to presenting real business strategies, I was able to show how data isn't just about math—it's about making changes that help the business. The insights found here show how looking closely at data can optimise shipping, marketing, and customer happiness.

<br>

## 🙏 Acknowledgments

---

Thank you for taking the time to review my project!

A special thanks to **Olist** and the **Kaggle community** for sharing this great dataset. It is an amazing resource for practicing with real-world data problems.

If you have any feedback, suggestions, or just want to chat about data, analytics, and business strategy, please feel free to reach out!

<br>


<br>

## 👨‍💻 Author  

---

**[Animesh Sanghi](Animesh_Resume.pdf)** | *Data Analyst | MBA '28 (Analytics & Data Science) MUJ*  
9406570600 | animeshsanghi.da@gmail.com | [LinkedIn Profile](https://www.linkedin.com/in/animeshsanghi-da/) | [GitHub Profile](https://github.com/animeshsanghi-da)