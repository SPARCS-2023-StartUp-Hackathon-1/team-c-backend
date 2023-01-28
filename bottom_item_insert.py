from main import musinsa_crawling
from db_initialize import get_database

def add_items(site_url):
    dbname = get_database()
    collection_name = dbname["denim_pants_items"]
    
    item_info = musinsa_crawling(site_url)
    
    item_1 = {
        "name" : item_info[0],
        "fit" : item_info[1],
        "texture" : item_info[2],
        "stretch" : item_info[3],
        "transparency" : item_info[4],
        "thickness" : item_info[5]
    }
    
    