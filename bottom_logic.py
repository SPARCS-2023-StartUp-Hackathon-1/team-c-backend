from pymongo_get_database import get_database

def calc_score(product_name: str):
    
    total = 0
    
    dbname = get_database()
    collection_name = dbname['jacket_items']
    
    jackets = collection_name.find()
    for jacket in jackets:
        if jacket['name'] == product_name:
            if jacket['fit'] == "슬림 핏" or jacket['fit'] == "오버 핏":
                total+=0
            elif jacket['fit'] == "레귤러 핏":
                total+=20
            if jacket['length'] == "크롭 기장" or jacket['length'] == '롱 기장':
                total+=0
            elif jacket['length'] == "기본 기장":
                total+=20
            if jacket['neck_line'] == "높은 넥라인":
                total+=0
            elif jacket['neck_line'] == "보통 넥라인":
                total+=10
            elif jacket['neck_line'] == "파인 넥라인":
                total+=20
            if jacket['design'] == "화려함":
                total+=0
            elif jacket['design'] == "단조로움":
                total+=10
            elif jacket['design'] == "무지":
                total+=20
            if jacket['material'] == "트위드":
                total+=0
            elif jacket['material'] == "폴리에스터" or jacket['material'] == "스웨이드":
                total+=10
            elif jacket['material'] == "울" or jacket['material'] == "캐새미어" or jacket['material'] == "천연가죽" or jacket['material'] == "코튼" or jacket['material'] == "데님":
                total+=20   
    
    print(str(total) + "%")

if __name__=="__main__":
    product_name = str(input("자켓 상품명을 입력하세요: "))
    calc_score(product_name)