from main import musinsa_crawling
from db_initialize import get_database

def add_items():
    dbname = get_database()
    collection_name = dbname["denim_pants_items"]
    
    item_1_info = musinsa_crawling("https://www.musinsa.com/app/goods/1540151")
    item_2_info = musinsa_crawling("https://www.musinsa.com/app/goods/2737165")

    item_1 = {
        "name" : item_1_info[0],
        "fit" : item_1_info[1],
        "texture" : item_1_info[2],
        "stretchiness" : item_1_info[3],
        "transparency" : item_1_info[4],
        "thickness" : item_1_info[5],
        "price" : int(item_1_info[6]),
        "image1_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/denim_pants/item_1/image1.jpg",
        "image1_URI" : "s3://sparcs-2023-startup-hackathon-c-1/denim_pants/item_1/image1.jpg",
        "image2_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/denim_pants/item_1/image2.jpg",
        "image2_URI" : "s3://sparcs-2023-startup-hackathon-c-1/denim_pants/item_1/image2.jpg",
        "image3_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/denim_pants/item_1/image3.jpg",
        "image3_URI" : "s3://sparcs-2023-startup-hackathon-c-1/denim_pants/item_1/image3.jpg",
        "image4_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/denim_pants/item_1/image4.jpg",
        "image4_URI" : "s3://sparcs-2023-startup-hackathon-c-1/denim_pants/item_1/image4.jpg"
    }
    
    item_2 = {
        "name" : item_2_info[0],
        "fit" : item_2_info[1],
        "texture" : item_2_info[2],
        "stretchiness" : item_2_info[3],
        "transparency" : item_2_info[4],
        "thickness" : item_2_info[5],
        "price" : int(item_2_info[6]),
        "image1_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/denim_pants/item_2/image1.jpg",
        "image1_URI" : "s3://sparcs-2023-startup-hackathon-c-1/denim_pants/item_2/image1.jpg",
        "image2_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/denim_pants/item_2/image2.jpg",
        "image2_URI" : "s3://sparcs-2023-startup-hackathon-c-1/denim_pants/item_2/image2.jpg",
        "image3_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/denim_pants/item_2/image3.jpg",
        "image3_URI" : "s3://sparcs-2023-startup-hackathon-c-1/denim_pants/item_2/image3.jpg",
        "image4_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/denim_pants/item_2/image4.jpg",
        "image4_URI" : "s3://sparcs-2023-startup-hackathon-c-1/denim_pants/item_2/image4.jpg"
    }   

    collection_name.insert_many([item_1, item_2])
    
if __name__ == '__main__':
    add_items()
