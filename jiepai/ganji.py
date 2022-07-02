# encoding: utf-8


import pymongo
import requests
from bs4 import BeautifulSoup


# url = 'https://www.sinotrade.com.tw/'
url = 'http://www.ganji.com'
client = pymongo.MongoClient('localhost', 27017)
data58 = client['data58']
url_list = data58['url_list']


def get_html(url):
    web_data = requests.get(url)
    print(web_data.text)
    soup = BeautifulSoup(web_data.text, 'lxml')
    titles = soup.select('div#wrapper div.f-hot dl dd i a')
    links = soup.select('div#wrapper div.f-hot dl dd i a')
    link = links.get('href')
    url_list.insert_one({'titles': titles, 'link': link})
    print(url_list)


if __name__ == '__main__':
    get_html(url)
