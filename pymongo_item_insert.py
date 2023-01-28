from pymongo_get_database import get_database
from bson import ObjectId
from PIL import Image
import io

def insert_image():

    im = Image.open("img/item_1/image.png")
    
    image_bytes = io.BytesIO()
    im.save(image_bytes, format='PNG')

def add_items():
    
    dbname = get_database()
    collection_name = dbname["jacket_items"]
    
    im1 = Image.open("img/item_1/image.png")
    
    item_1_image_bytes = io.BytesIO()
    im1.save(item_1_image_bytes, format='PNG')
    
    """item_1 = {
        "name" : "레이나 트위드자켓",
        "fit" : "레귤러 핏",
        "length" : "기본 기장",
        "neck_line" : "높은 넥라인",
        "design" : "단조로움",
        "material" : "트위드",
        "image_data" : item_1_image_bytes.getvalue()
    }
    
    item_2 = {
        "name" : "엔니드 카라 트위드 자켓",
        "fit" : "레귤러 핏",
        "length" : "기본 기장",
        "neck_line" : "보통 넥라인",
        "design" : "무지",
        "material" : "트위드",
        "image_data" :
    }

    item_3 = {
        "name" : "Moring jacket (말차)",
        "fit" : "오버 핏",
        "length" : "롱 기장",
        "neck_line" : "파인 넥라인",
        "design" : "무지",
        "material" : "울",
        "image_data" :
    }
    
    item_4 = {
        "name" : "도넬 세미크롭 자켓",
        "fit" : "레귤러 핏",
        "length" : "기본 기장",
        "neck_line" : "파인 넥라인",
        "design" : "무지",
        "material" : "폴리에스터",
        "image_data" :
    }
    
    item_5 = {
        "name" : "루닝 라운드 트위드 자켓",
        "fit" : "레귤러 핏",
        "length" : "크롭 기장",
        "neck_line" : "보통 넥라인",
        "design" : "단조로움",
        "material" : "트위드",
        "image_data" :
    }
    
    collection_name.insert_many([item_1, item_2, item_3, item_4, item_5])"""
    
if __name__ == "__main__":   
    add_items()