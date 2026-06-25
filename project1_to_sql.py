import pandas as pd
import sqlite3

try:
    print("🔄 Initializing Data Ingestion Pipeline: CSV to SQL Database...")
    
    # 1. Extract: Load the cleaned dataset into a Pandas DataFrame
    source_file = 'Sample - Superstore.csv'
    df = pd.read_csv(source_file, encoding='latin1')
    print(f"✅ Successfully extracted {len(df)} rows from '{source_file}'.")
    
    # 2. Establish Connection: Connect to SQLite Target Database
    db_name = 'Superstore_DB.db'
    conn = sqlite3.connect(db_name)
    print(f"📡 Connection established with Target Database: '{db_name}'")
    
    # 3. Load: Write records to SQL Table (Replaces table if it already exists)
    table_name = 'superstore_table'
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    print(f"📦 Data successfully loaded into SQL table: '{table_name}'.")
    
    # 4. Cleanup: Close database connection safely
    conn.close()
    print("🔒 Database connection closed securely. Pipeline execution complete.")

except FileNotFoundError:
    print(f"❌ Critical Error: Source file '{source_file}' not found. Check file path.")
except Exception as e:
    print(f"❌ Pipeline Execution Failed: {e}")

