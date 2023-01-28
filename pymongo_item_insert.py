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
    
    item_2 = {
        "name" : "엔니드 카라 트위드 자켓",
        "fit" : "레귤러 핏",
        "length" : "기본 기장",
        "neck_line" : "보통 넥라인",
        "design" : "무지",
        "material" : "트위드"
    }

    item_3 = {
        "name" : "Moring jacket (말차)",
        "fit" : "오버 핏",
        "length" : "롱 기장",
        "neck_line" : "파인 넥라인",
        "design" : "무지",
        "material" : "울"
    }
    
    item_4 = {
        "name" : "도넬 세미크롭 자켓",
        "fit" : "레귤러 핏",
        "length" : "기본 기장",
        "neck_line" : "파인 넥라인",
        "design" : "무지",
        "material" : "폴리에스터"
    }
    
    item_5 = {
        "name" : "루닝 라운드 트위드 자켓",
        "fit" : "레귤러 핏",
        "length" : "크롭 기장",
        "neck_line" : "보통 넥라인",
        "design" : "단조로움",
        "material" : "트위드"
    }
    
    collection_name.insert_many([item_1, item_2, item_3, item_4, item_5])
    
if __name__ == "__main__":   
    add_items()