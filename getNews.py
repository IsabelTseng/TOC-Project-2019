import requests #引入函式庫
from bs4 import BeautifulSoup
import re

def getNews1():
    url = 'http://www.peoplenews.tw/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
    resp = requests.get(url, headers=headers)

    soup = BeautifulSoup(resp.text, 'html.parser')
    area_realtime = soup.find_all('div', id = 'area_realtime')
    news_title = soup.find_all('div', class_ = 'title')
    titles = ['民報 即時新聞：']
    for index, item in enumerate(news_title):
        titles.append("{0:2d}. {1}".format(index + 1, item.text.strip()))
        # print("{0:2d}. {1}".format(index + 1, item.text.strip()))
    return titles.copy()

# news1 = getNews1()
# print('\n'.join(news1))

def getNews2():
    url = 'https://newtalk.tw/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
    resp = requests.get(url, headers=headers)

    soup = BeautifulSoup(resp.text, 'html.parser')
    news_title = soup.find_all('div', re.compile(''))
    titles = ['New Talk 前五頭條：']
    for index, item in enumerate(news_title):
        titles.append("{0:2d}. {1}".format(index + 1, item.text.strip()))
    return titles.copy()

# news2 = getNews2()
# print('\n'.join(news2))