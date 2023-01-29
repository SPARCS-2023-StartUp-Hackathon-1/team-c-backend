# [TEAM C] Repository - Backend

Team C 백엔드 부분을 담당하는 레포지토리입니다.

다음과 같은 기능이 포함되어 있습니다.
- 비지니스 로직과 아이템 DB 저장, 쿼리 및 배포 담당
- 앱 데모에 필요한 모든 옷 이미지들을 Amazon S3 버킷에 저장하고 Public Access가 가능하도록 하여 MongoDB Atlas에는 이 이미지들의 Object URL만을 JSON 형태로 저장
- MongoDB Query를 사용해 프런트엔드에 원하는 이미지 S3 Object URL 제공 
- 각 옷들의 세부 데이터 또한 PyMongo를 통해 MongoDB에 저장 
- BeautifulSoup를 활용하여 무신사 홈페이지를 크롤링하여 각 상품의 이름, 가격, 핏, 소재, 신축성, 등등이 자동으로 파싱되어 로직
- 본 앱의 추천 서비스를 통해 유저가 좋아요를 클릭한 옷이 그 유저에게 얼마나 어울리나 핏, 기장, 디자인 등등을 각자의 개체로 인식하여 점수를 더해 자동으로 퍼센트를 계산해주는 로직

## 프로젝트에서 사용한 기술
- Amazon S3
- Flask
- PyMongo
- AI Platform (Naver Cloud Platform)
- MongoDB Atlas
- BeautifulSoup (무신사 크롤링)
```python
    soup = BeautifulSoup(test, 'html.parser')
    product_title = soup.find(class_="product_title")
    
    #To find 2nd occurence of \n in order to substring the product title
    occurence = find_substring(product_title.text, "\n", 1)
    item_info.append(product_title.text[1 : occurence])

    site_data = soup.select('.table-simple .active')
    guide_title = soup.select('.table-simple th')
    
    for (i, s) in itertools.zip_longest(guide_title, site_data):
        count += 1
        if i is None:
            get_data = s.text.replace('  ', '').replace('\n', '') 
        else:
            get_title = i.text.replace('  ', '').replace('\n', '')
            get_data = s.text.replace('  ', '').replace('\n', '')
            item_info.append(get_data)
            
            if count == 5:
                break
    guide_title = soup.find(class_="price-del").text
    get_price = guide_title[0:2] + guide_title[3:len(guide_title)-1]
    item_info.append(get_price)
``` 

## Python 종속 항목 지정
```
1. Python3
Make sure Python3 is installed and check its version with python3 -V

2. Requirements
pip install -r requirements.txt
```

## 배포 방법
```
1. Clone the repository 
git clone https://github.com/SPARCS-2023-StartUp-Hackathon-1/team-c-backend.git

2. Save item information to MongoDB
python3 top_item_insert.py
python3 bottom_item_insert.py

3. Run logic by inputting item name
python3 top_logic.py
python3 bottom_logic.py
```

## 환경 변수 및 시크릿
- MongoDB_Username
- MongoDB_Password