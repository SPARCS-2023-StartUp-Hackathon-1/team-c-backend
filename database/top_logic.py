from db_initialize import get_database

def calc_score(product_name: str):
    
    total = 0
    
    dbname = get_database()
    collection_name = dbname['jacket_items']
    
    jackets = collection_name.find()
    for jacket in jackets:
        if jacket['name'] == product_name:
            if jacket['fit'] == "레귤러 핏":
                total+=20
            if jacket['length'] == "기본 기장":
                total+=20
            if jacket['neck_line'] == "보통 넥라인" or jacket['neck_line'] == "카라넥":
                total+=10
            elif jacket['neck_line'] == "파인 넥라인":
                total+=20
            if jacket['design'] == "단조로움":
                total+=10
            elif jacket['design'] == "무지":
                total+=20
            if jacket['material'] == "폴리에스터" or jacket['material'] == "스웨이드":
                total+=10
            elif jacket['material'] == "울" or jacket['material'] == "캐새미어" or jacket['material'] == "천연가죽" or jacket['material'] == "코튼" or jacket['material'] == "데님":
                total+=20   
    
    print(str(total)+"%")
    return total

if __name__=="__main__":
    product_name = str(input("자켓 상품명을 입력하세요: "))
    calc_score(product_name)