# encoding: utf-8
# spider是代表一个爬虫

import json
import re
from multiprocessing import Pool

import pymongo
import requests
from requests.exceptions import RequestException

client = pymongo.MongoClient('localhost', 27017)
data58 = client['data58']
url_maoyan = data58['url_maoyan']


# 定义一个单页请求函数
def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?>integer">(.*?)</i>.*?</i>.*?fraction">(.*?)</i>.*?<dd>', re.S)

    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5].strip()[6]
        }


def write_to_file(content):
    with open('result.txt', 'a', 'encoding: utf-8') as f:
        f.wirte(json.dumps(content), + '\n')
        f.close()


def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    main(3)
