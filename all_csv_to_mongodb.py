import pandas as pd
from pymongo import MongoClient
import glob
import os

# Configuration
MONGO_URI = 'mongodb+srv://sruthypriyankapanigrahi123:Sruthy123456@cluster0.gn21n1r.mongodb.net/'
DB_NAME = 'mydatabase'

try:
    # MongoDB connection
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    
    # Get all CSV files
    csv_files = glob.glob('*.csv')
    
    for csv_file in csv_files:
        # Use filename (without extension) as collection name
        collection_name = os.path.splitext(csv_file)[0]
        collection = db[collection_name]
        
        # Read CSV file
        df = pd.read_csv(csv_file)
        records = df.to_dict('records')
        
        # Insert data to MongoDB
        collection.insert_many(records)
        print(f"Inserted {len(records)} records from {csv_file} to collection '{collection_name}'")
    
    print("All CSV files processed successfully!")
    
except Exception as e:
    print(f"Error: {e}")
finally:
    client.close()