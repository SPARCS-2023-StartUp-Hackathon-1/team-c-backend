import itertools
import requests
from bs4 import BeautifulSoup

def find_substring(txt, str1, n):
    parts = txt.split(str1, n + 1)
    if len(parts) <= n + 1:
        return -1
    return len(txt) - len(parts[-1]) - len(str1)

def musinsa_crawling(site_url: str):
    count = 0
    item_info = []
    
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/104.0.0.0 Safari/537.36'}
    
    test = requests.get(site_url, headers=headers).text
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
            #print(', ' + get_data, end='', flush=True)
        else:
            get_title = i.text.replace('  ', '').replace('\n', '')
            get_data = s.text.replace('  ', '').replace('\n', '')
            item_info.append(get_data)
            #print(get_title + ": " + get_data)
            
            if count == 5:
                break
            '''
            if count == 6:
                 print(get_title + ": " + get_data, end='')
            else:
                print(get_title + ": " + get_data) 
            '''
            
    guide_title = soup.find(class_="price-del").text
    get_price = guide_title[0:2] + guide_title[3:len(guide_title)-1]
    item_info.append(get_price)
    
    #print(item_info)
    return item_info

if __name__ == '__main__':
    url = input("크롤링 할 무신사 사이트 URL을 입력하세요: ")
    musinsa_crawling(url)
    