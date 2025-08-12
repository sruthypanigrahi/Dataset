# CSV to MongoDB Data Migration

Simple Python scripts to push CSV data to MongoDB.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Update MongoDB connection in the script files with your credentials.

## Usage

### Single CSV File
```bash
python excel_to_mongodb.py
```
Pushes `distribution_centers.csv` to MongoDB.

### All CSV Files
```bash
python all_csv_to_mongodb.py
```
Processes all CSV files in the folder and creates separate collections for each.

## Files
- `distribution_centers.csv`, `inventory_items.csv`, etc. - Data files
- `excel_to_mongodb.py` - Single file processor
- `all_csv_to_mongodb.py` - Batch processor
- `requirements.txt` - Dependencies