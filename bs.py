import requests
from bs4 import BeautifulSoup as bs
from urls import *


page = requests.get(TBATE_URL).content
soup = bs(page, 'lxml')
# chs=soup.find_all('div', class_='js-load-chapters')
print(soup.find_all('div',class_='container mt-10')[0])