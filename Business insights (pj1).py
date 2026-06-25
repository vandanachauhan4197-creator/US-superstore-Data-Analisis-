import pandas as pd

try:
    print("🔄 Analyzing business metrics, please wait...\n")
    df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')
    
    print("=========================================")
    print("💼 ADVANCED BUSINESS INSIGHTS REPORT")
    print("=========================================\n")

    # QUESTION 1: Who are our Top 5 Customers by Sales?
    print("👥 1. TOP 5 HIGH-VALUE CUSTOMERS:")
    top_customers = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(5)
    for name, sales in top_customers.items():
        print(f"   • {name}: ${round(sales, 2):,}")
    print("-" * 45)

    # QUESTION 2: Which Top 5 Products are causing the most Financial Loss?
    print("\n🚨 2. TOP 5 LOSS-MAKING PRODUCTS (Action Required):")
    # Sub-Category ke hisaab se sabse zyada loss wali cheezein dhoodhna
    worst_products = df.groupby('Sub-Category')['Profit'].sum().sort_values(ascending=True).head(5)
    for sub_cat, profit in worst_products.items():
        print(f"   • {sub_cat}: ${round(profit, 2):,}")
    print("-" * 45)

    # QUESTION 3: Shipping Mode Efficiency Analysis
    print("\n📦 3. SHIPPING MODE PERFORMANCE (Sales & Profitability):")
    ship_analysis = df.groupby('Ship Mode')[['Sales', 'Profit']].sum().sort_values(by='Sales', ascending=False)
    
    # Isko sundar format me table ki tarah print karwayenge
    print(ship_analysis.applymap(lambda x: f"${x:,.2f}"))
    print("-" * 45)

    print("\n✅ Business insights generated successfully! Ready for the presentation, Bhai!")

except FileNotFoundError:
    print("❌ Error: 'Sample - Superstore.csv' file not found.")
except Exception as e:
    print(f"❌ An error occurred: {e}")
