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
        "material" : "트위드",
        "price" : 73520,
        "image1_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_1/image1.png",
        "image1_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_1/image1.png",
        "image2_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_1/image2.jpg",
        "image2 URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_1/image2.jpg",
        "image3_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_1/image3.jpg",
        "image3_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_1/image3.jpg",
        "image4_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_1/image4.jpg",
        "image4_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_1/image4.jpg"
    }
    
    item_2 = {
        "name" : "엔니드 카라 트위드 자켓",
        "fit" : "레귤러 핏",
        "length" : "기본 기장",
        "neck_line" : "보통 넥라인",
        "design" : "무지",
        "material" : "트위드",
        "price" : 56950,
        "image1_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_2/image1.png",
        "image1_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_2/image1.png",
        "image2_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_2/image2.jpg",
        "image2_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_2/image2.jpg",
        "image3_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_2/image3.jpg",
        "image3_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_2/image3.jpg",
        "image4_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_2/image4.jpg",
        "image4_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_2/image4.jpg"
    }

    item_3 = {
        "name" : "Moring jacket (말차)",
        "fit" : "오버 핏",
        "length" : "롱 기장",
        "neck_line" : "파인 넥라인",
        "design" : "무지",
        "material" : "울",
        "price" : 86700,
        "image1_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_3/image1.png",
        "image1_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_3/image1.png",
        "image2_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_3/image2.jpg",
        "image2_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_3/image2.jpg",
        "image3_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_3/image3.jpg",
        "image3_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_3/image3.jpg",
        "image4_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_3/image4.jpg",
        "image4_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_3/image4.jpg"
    }
    
    item_4 = {
        "name" : "도넬 세미크롭 자켓",
        "fit" : "레귤러 핏",
        "length" : "기본 기장",
        "neck_line" : "파인 넥라인",
        "design" : "무지",
        "material" : "폴리에스터",
        "price" : 46430,
        "image1_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_4/image1.png",
        "image1_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_4/image1.png",
        "image2_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_4/image2.jpg",
        "image2_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_4/image2.jpg",
        "image3_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_4/image3.jpg",
        "image3_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_4/image3.jpg",
        "image4_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_4/image4.jpg",
        "image4_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_4/image4.jpg"
    }
    
    item_5 = {
        "name" : "루닝 라운드 트위드 자켓",
        "fit" : "레귤러 핏",
        "length" : "크롭 기장",
        "neck_line" : "보통 넥라인",
        "design" : "단조로움",
        "material" : "트위드",
        "price" : 32400,
        "image1_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_5/image1.png",
        "image1_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_5/image1.png",
        "image2_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_5/image2.jpg",
        "image2_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_5/image2.jpg",
        "image3_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_5/image3.jpg",
        "image3_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_5/image3.jpg",
        "image4_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_5/image4.jpg",
        "image4_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_5/image4.jpg"
    }
        
    item_6 = {
        "name" : "WOMEN 크롭 오버핏 마일드레더 블레이저 가죽자켓",
        "price" : 71910,
        "image1_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_6/image1.jpg",
        "image1_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_6/image1.jpg",
        "image2_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_6/image2.jpg",
        "image2_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_6/image2.jpg",
        "image3_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_6/image3.jpg",
        "image3_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_6/image3.jpg",
        "image4_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_6/image4.jpg",
        "image4_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_6/image4.jpg"
    }
    
    item_7 =  {
        "name" : "아로 크롭 숏 블레이저 브이넥 무지 노카라 자켓",
        "price" : 44100,
        "image1_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_7/image1.jpg",
        "image1_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_7/image1.jpg",
        "image2_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_7/image2.jpg",
        "image2_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_7/image2.jpg",
        "image3_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_7/image3.jpg",
        "image3_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_7/image3.jpg",
        "image4_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_7/image4.jpg",
        "image4_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_7/image4.jpg"
    }
    
    item_8 = {
        "name" : "세미 크롭 원버튼 자켓 블레이져",
        "price" : 39330,
        "image1_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_8/image1.jpg",
        "image1_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_8/image1.jpg",
        "image2_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_8/image2.jpg",
        "image2_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_8/image2.jpg",
        "image3_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_8/image3.jpg",
        "image3_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_8/image3.jpg",
        "image4_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_8/image4.jpg",
        "image4_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_8/image4.jpg"
    }
    
    item_9 = {
        "name" : "고퀄리티 런던 패드 금장버튼 트위드 숏 여자 자켓 가을코디 간절기룩",
        "price" : 133870,
        "image1_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_9/image1.jpg",
        "image1_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_9/image1.jpg",
        "image2_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_9/image2.jpg",
        "image2_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_9/image2.jpg",
        "image3_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_9/image3.jpg",
        "image3_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_9/image3.jpg",
        "image4_URL" : "https://sparcs-2023-startup-hackathon-c-1.s3.ap-northeast-2.amazonaws.com/item_9/image4.jpg",
        "image4_URI" : "s3://sparcs-2023-startup-hackathon-c-1/item_9/image4.jpg"
    }
    
    collection_name.insert_many([item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9])
    
if __name__ == "__main__":   
    add_items()