import itertools
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
  
def musinsa_crawling():
    count = 0
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/104.0.0.0 Safari/537.36'}
    '''나중에 site url을 function argument로 넣어서 자동화 할 예정'''
    site_url = "https://www.musinsa.com/app/goods/2731596"
    test = requests.get(site_url, headers=headers).text
    soup = BeautifulSoup(test, 'html.parser')
    
    product_title = soup.find(class_="product_title")
    print(product_title.text)
    
    site_data = soup.select('.table-simple .active')
    guide_title = soup.select('.table-simple th')
    
    for i in guide_title:
        get_txt = i.text.replace('  ', '').replace('\n', '')
        print(get_txt)     
        
    for s in site_data:         
        get_txt = s.text.replace('  ', '').replace('\n', '')
        print(get_txt)
        
if __name__ == '__main__':
    musinsa_crawling()


