import sqlite3
import pandas as pd

try:
    print("📡 Connecting to 'Superstore_DB.db' Engine...")
    conn = sqlite3.connect('Superstore_DB.db')
    
    print("==================================================")
    print("📊 ADVANCED RELATIONAL ANALYTICS REPORT (SQL)")
    print("==================================================\n")

    # -------------------------------------------------------------------
    # USE CASE 1: Identify High-Value Categories by Average Profit Margin
    # -------------------------------------------------------------------
    print("📝 Analysis 1: Grouping Categories by Average Profitability...")
    
    query_1 = """
    SELECT 
        Category, 
        ROUND(AVG(Sales), 2) AS Avg_Sales,
        ROUND(AVG(Profit), 2) AS Avg_Profit,
        ROUND((SUM(Profit) / SUM(Sales)) * 100, 2) AS Profit_Margin_Percent
    FROM superstore_table
    GROUP BY Category
    ORDER BY Profit_Margin_Percent DESC;
    """
    
    result_1 = pd.read_sql_query(query_1, conn)
    print(result_1)
    print("-" * 60)

    # -------------------------------------------------------------------
    # USE CASE 2: Sub-Category Performance Analysis within Technology
    # -------------------------------------------------------------------
    print("\n📝 Analysis 2: Filtering & Sorting Sub-Categories (Technology Only)...")
    
    query_2 = """
    SELECT 
        [Sub-Category], 
        ROUND(SUM(Sales), 2) AS Total_Sales,
        ROUND(SUM(Profit), 2) AS Total_Profit
    FROM superstore_table
    WHERE Category = 'Technology'
    GROUP BY [Sub-Category]
    ORDER BY Total_Profit DESC;
    """
    
    result_2 = pd.read_sql_query(query_2, conn)
    print(result_2)
    print("-" * 60)

    # -------------------------------------------------------------------
    # USE CASE 3: Analytical Window Function (Rank of States by Total Sales)
    # -------------------------------------------------------------------
    print("\n📝 Analysis 3: Fetching Top 5 Markets using ROW_NUMBER() Window Function...")
    
    query_3 = """
    SELECT * FROM (
        SELECT 
            State,
            ROUND(SUM(Sales), 2) AS State_Sales,
            ROW_NUMBER() OVER (ORDER BY SUM(Sales) DESC) AS Sales_Rank
        FROM superstore_table
        GROUP BY State
    ) AS Ranked_States
    WHERE Sales_Rank <= 5;
    """
    
    result_3 = pd.read_sql_query(query_3, conn)
    print(result_3)
    print("-" * 60)

    # Closing connection safely
    conn.close()
    print("\n🔒 Analytical reporting complete. Connection closed securely.")

except Exception as e:
    print(f"❌ Execution Failed: {e}")
