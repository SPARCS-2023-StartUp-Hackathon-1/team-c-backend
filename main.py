import itertools
import requests
from bs4 import BeautifulSoup
  
def musinsa_crawling(site_url):
    
    count = 0
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/104.0.0.0 Safari/537.36'}
    
    test = requests.get(site_url, headers=headers).text
    soup = BeautifulSoup(test, 'html.parser')
    
    product_title = soup.find(class_="product_title")
    print(product_title.text)
    
    site_data = soup.select('.table-simple .active')
    guide_title = soup.select('.table-simple th')
        
    for (i, s) in itertools.zip_longest(guide_title, site_data):
        count += 1
        if i is None:
            get_data = s.text.replace('  ', '').replace('\n', '') 
            print(', ' + get_data, end='', flush=True)
        else:
            get_title = i.text.replace('  ', '').replace('\n', '')
            get_data = s.text.replace('  ', '').replace('\n', '')
            if count == 6:
                 print(get_title + ": " + get_data, end='')
            else:
                print(get_title + ": " + get_data) 
    print()
    print()
        
if __name__ == '__main__':
    url = input("크롤링 할 무신사 사이트 URL을 입력하세요: ")
    musinsa_crawling(url)


