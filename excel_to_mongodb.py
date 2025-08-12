import pandas as pd
from pymongo import MongoClient
import os
from dotenv import load_dotenv  # Import dotenv

# Load environment variables from .env file
load_dotenv()

# Read variables from .env
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
EXCEL_FILE = os.getenv("EXCEL_FILE")

try:
    # MongoDB connection
    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    
    # Read CSV file
    df = pd.read_csv(EXCEL_FILE)
    
    # Convert DataFrame to dictionary records
    records = df.to_dict('records')
    
    # Insert data to MongoDB
    collection.insert_many(records)
    
    print(f"Successfully inserted {len(records)} records to MongoDB")
    
except Exception as e:
    print(f" Error: {e}")
    
finally:
    client.close()
