from pymongo_get_database import get_database

def add_items():
    
    dbname = get_database()
    collection_name = dbname["jacket_items"]
    
    item_1 = {
        "name" : "레이나 트위드자켓",
        "fit" : "레귤러 핏",
        "length" : "기본 기장",
        "neck_line" : "높은 넥라인",
        "design" : "단조로움",
        "material" : "트위드"
    }
    
    collection_name.insert_one(item_1)