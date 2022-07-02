# encoding: utf-8
import json
from urllib.parse import urlencode
import pymongo
import requests
from bs4 import BeautifulSoup
from requests import RequestException


client = pymongo.MongoClient('localhost', 27017)
data58 = client['data58']
url_toutiao = data58['url_toutiao']


def get_page_index(offset, keyword):
    data = {
        "aid": "24",
        "app_name": "web_search",
        "offset": offset,
        "format": "json",
        "keyword": keyword,
        "autoload": "true",
        "count": "20",
        "en_qc": "1",
        "cur_tab": "1",
        "from": "search_tab",
        "pd": "synthesis",
        "timestamp": "1580698716499"
    }

    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print('请求索引出错')
        return None


def parse_page_index(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')
            url_toutiao.insert({'article': 'article_url'})


article_img = '''
    http://toutiao.com/group/6789399245024657934/
    http://toutiao.com/group/6777243413981954575/
    http://toutiao.com/group/6609426526892982798/
    http://toutiao.com/group/6783458351016575500/
    https://apis.fengniao.com/index.php?r=rss/news/detail&source=2&type=1&id=10927284
    http://toutiao.com/group/6760980286252515853/
    http://toutiao.com/group/6773219752874607108/
    http://toutiao.com/group/6772346555409105416/
    http://toutiao.com/group/6673416133837586958/
    http://toutiao.com/group/6774540258336834056/
    http://toutiao.com/group/6781742051445703172/
    http://toutiao.com/group/6613248239443378695/
    http://toutiao.com/group/6776493069714850315/
    http://toutiao.com/group/6789405877347549710/
    http://toutiao.com/group/6789027354917208590/
'''


def parse_page_detail(html):
    soup = BeautifulSoup(html, 'lxml')
    title = soup.select('title')[0].text
    print(title)


def main():
    html = get_page_index(0, '街拍')
    for url in parse_page_index(html):
        print(url)


if __name__ == '__main__':
    main()
