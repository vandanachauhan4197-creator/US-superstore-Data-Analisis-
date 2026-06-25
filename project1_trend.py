import pandas as pd
import matplotlib.pyplot as plt

try:
    print("🔄 Loading data for Trend Chart...")
    df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')
    
    # Date formatting
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    df['Year'] = df['Order Date'].dt.year # Sirf Year nikal rahe hain taaki crash na ho

    # Grouping by Year
    yearly_sales = df.groupby('Year')['Sales'].sum()

    # Plotting Line Chart
    plt.figure(figsize=(8, 5))
    plt.plot(yearly_sales.index.astype(str), yearly_sales.values, marker='o', color='#17a2b8', linewidth=2)
    plt.title('Yearly Sales Trend', fontsize=14, fontweight='bold')
    plt.xlabel('Year')
    plt.ylabel('Total Sales ($)')
    plt.grid(True, linestyle='--')
    plt.tight_layout()

    print("🚀 Opening Year-wise Trend Chart...")
    plt.show()

except Exception as e:
    print(f"❌ Error: {e}")
