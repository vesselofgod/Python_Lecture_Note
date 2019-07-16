import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.naver.com/')
html=r.text
soup=BeautifulSoup(html,'html.parser')

hot_keyword = soup.select('.ah_k')

for title in hot_keyword:
    print(title.text)
