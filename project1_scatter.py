import pandas as pd
import matplotlib.pyplot as plt

try:
    print("🔄 Loading data for Scatter Plot...")
    df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')

    # Plotting Scatter Plot
    plt.figure(figsize=(8, 5))
    plt.scatter(df['Sales'], df['Profit'], alpha=0.5, color='#6f42c1')
    plt.title('Sales vs Profit Relationship', fontsize=14, fontweight='bold')
    plt.xlabel('Sales ($)')
    plt.ylabel('Profit ($)')
    plt.axhline(0, color='red', linestyle='--')
    plt.grid(True, linestyle='--')
    plt.tight_layout()

    print("🚀 Opening Sales vs Profit Scatter Plot...")
    plt.show()

except Exception as e:
    print(f"❌ Error: {e}")
