import requests #引入函式庫
from bs4 import BeautifulSoup
import re

def getTop10Title(number):
    url = 'https://www.dcard.tw/f'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
    resp = requests.get(url, headers=headers)

    soup = BeautifulSoup(resp.text, 'html.parser')
    dcard_title = soup.find_all('h3', re.compile('PostEntry_title_'))
    titles = ['Dcard 熱門前十文章標題：']
    for index, item in enumerate(dcard_title[:number]):
        titles.append("{0:2d}. {1}".format(index + 1, item.text.strip()))
    return titles.copy()

# dcard10Title = getTop10Title(10)
# print('\n'.join(dcard10Title))