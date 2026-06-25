import pandas as pd
import matplotlib.pyplot as plt

try:
    print("🔄 Loading data for Segment Chart...")
    df = pd.read_csv('Sample - Superstore.csv', encoding='latin1')
    
    segment_share = df.groupby('Segment')['Sales'].sum()

    # Plotting Pie Chart
    plt.figure(figsize=(6, 6))
    colors = ['#ff9999','#66b3ff','#99ff99']
    plt.pie(segment_share.values, labels=segment_share.index, autopct='%1.1f%%', colors=colors, startangle=90)
    plt.title('Sales Share by Customer Segment', fontsize=14, fontweight='bold')
    plt.tight_layout()

    print("🚀 Opening Segment Pie Chart...")
    plt.show()

except Exception as e:
    print(f"❌ Error: {e}")
