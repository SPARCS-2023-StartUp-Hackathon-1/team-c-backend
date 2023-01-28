from pymongo_get_database import get_database

def calc_score(product_name: str):
    
    total = 0
    
    dbname = get_database()
    collection_name = dbname['denim_pants_items']
    
    denim_pants = collection_name.find()
    for pant in denim_pants:
        if pant.name == product_name:
            if pant.fit == "슬림" or pant.fit == "루즈":
                total+=10
            elif pant.fit == "레귤러":
                total+=20
            if pant.texture == "약간 부드러움" or pant.texture == "약간 뻣뻣함":
                total+=10
            elif pant.texture == "보통":
                total+=20
            if pant.stretchiness == "거의 없음" or pant.stretchiness == "약간 있음":
                total+=10
            elif pant.stretchiness == "보통":
                total+=20
            if pant.transparency == "보통":
                total+=10
            elif pant.transparency == "거의 없음" or pant.transparency == "없음":
                total+=20
            if pant.thickness == "약간 얇음" or pant.thickness == "약간 두꺼움":
                total+=10
            elif pant.thickness == "보통":
                total+=20
                
    print(str(total) + "%")

if __name__=="__main__":
    product_name = str(input("자켓 상품명을 입력하세요: "))
    calc_score(product_name)