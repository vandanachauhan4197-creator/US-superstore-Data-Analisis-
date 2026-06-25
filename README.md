# US Superstore End-to-End Data Analytics Pipeline

An advanced, end-to-end data analytics project that demonstrates a complete ETL (Extract, Transform, Load) pipeline using Python, structural process automation, and relational database reporting using Advanced SQL. 

The project bridges the gap between technical data engineering and digital marketing/business growth frameworks, providing actionable insights from historical retail data.

---

## 🚀 Key Features & Architectural Workflow

1. **Automated ETL Pipeline (Python & Pandas):** * **Extraction & Cleaning:** Processes raw unstructured or semi-structured transactional datasets (`Sample - Superstore.csv`).
   * **Data Cleansing:** Handles missing data, fixes data types, structures date fields, and eliminates anomalies.
   * **Data Ingestion:** Automates structural pipeline ingestion, converting cleaned DataFrames directly into a relational database structure (`Superstore_DB.db`).

2. **Advanced Relational Business Reporting (SQL):**
   * Utilizes **Window Functions**, **CTEs (Common Table Expressions)**, and structural joins to track product performance, customer segmentation, and market trends.
   * Tailored for **Digital Marketing Analytics**, tracking metrics like Customer Lifetime Value (CLV) trends, high-value consumer segments, and seasonal sales velocity.

---

## 📁 Repository Structure & File Description

To keep the development production-ready and modular, the repository is split into distinct logical scripts:

* 🛠️ **`project1.py(Python cleaning)`** – Core script handles data preprocessing, clearing anomalies, and setting up initial data frameworks.
* 📊 **`project1.py(Visualising the cleared data)`** – Performs exploratory data analysis (EDA) to find out basic distributions and patterns.
* 📈 **`project1_trend.py`** – Tracks monthly/yearly sales velocity and performance shifts over time.
* 👥 **`project1_segment.py`** – Segments consumer demographics to identify target audiences for modern digital marketing frameworks.
* 📉 **`project1_scatter.py`** – Explores advanced correlations (e.g., Profit vs. Discount dynamics) to optimize pricing strategies.
* 🗄️ **`project1_to_sql.py`** – Ingestion script that automates writing the Python-processed data straight into SQLite tables.
* 🔍 **`project1_queries.py`** & **`Business insights (pj1).py`** – Advanced SQL analytical query scripts built for structural marketing and business reporting.
* 📦 **`Sample - Superstore.csv`** & **`Superstore_DB.db`** – The raw source transactional dataset and the compiled final relational database.

---

## 💡 Business & Digital Marketing Insights Covered

This project is built around real-world business objectives rather than just running code:
* **Product Performance Analytics:** Finding out which category drives volume vs. which drives margins.
* **Discount Optimization:** Analyzing the exact point where offering discounts hurts net profitability (using scatter metrics).
* **Target Audience Mapping:** Segmenting performance across modern demographics to optimize ad spend and lower acquisition costs.

---

## 🛠️ Tech Stack & Tools Used
* **Languages:** Python, Advanced SQL
* **Libraries:** Pandas, NumPy, Matplotlib, Seaborn
* **Database:** SQLite3 / MySQL architecture standards
* **Methodologies:** Prompt Engineering (Workflow Automation), Process Optimization, Functional Scripting
