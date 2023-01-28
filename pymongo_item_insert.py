from pymongo_get_database import get_database

def add_items():
    
    dbname = get_database()
    collection_name = dbname["jacket_items"]