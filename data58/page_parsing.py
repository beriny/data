# encoding: utf-8

import time

import pymongo
import requests
from bs4 import BeautifulSoup

client = pymongo.MongoClient('localhost', 27017)
db58 = client['data58']
url_list = db58['url_list']
item_info = db58['item_info']


# spider爬取所有的网页链接
def get_links_from(channel, pages, who_sells=0):
    # http://suqian.58.com/diannao/0/pn2
    list_view = '{}{}/pn{}/'.format(channel, str(who_sells), str(pages))
    web_html = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(web_html.text, 'lxml')
    # if soup.find('td', 't'):
    for link in soup.select('td.t a.t'):
        item_link = link.get('href').split('?')[0]
        url_list.insert_one({'url': item_link})
        print(item_link)
        return item_link


# # 将所有传入的数组解析成单个网页
# def get_single_page(**kwargs):
#     page_links = kwargs.split('/n')[0].text
#     for single_link in page_links:
#         print(single_link)
#     return single_link


# 从数据库中取出url，获得爬取的信息
def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    # no_longer_exist = '404' in soup.find('script', type="text/javascript")[0:].get_text('src')
    # no_longer_exist = '商品已下架' in soup.find('div', "button_li").get_text()
    # if no_longer_exist:
    #     pass
    # else:
    title = soup.title.text
    price = soup.select('span.infocard__container__item__main__text--price')[0].text
    data = soup.select('div.detail-title__info__text')[0].text
    area = list(soup.select('.c_25d a')[0].stripped_strings) if soup.find('span', 'c_25d') else None
    item_info.insert({'title': title, 'price': price, 'data': data, 'area': area})
    print({'title': title, 'price': price, 'data': data, 'area': area})


channel_links = '''
    https://suqian.58.com/jiadian/39788186669978x.shtml
    https://suqian.58.com/jiadian/39788169486731x.shtml
    https://suqian.58.com/jiadian/39788155283331x.shtml
    https://suqian.58.com/jiadian/39788135644172x.shtml
    https://suqian.58.com/jiadian/39788122093978x.shtml
    https://suqian.58.com/jiadian/39788085918235x.shtml
    https://suqian.58.com/jiadian/39788021037346x.shtml
    https://suqian.58.com/jiadian/39688270458758x.shtml
    https://suqian.58.com/jiadian/39688131537683x.shtml
    https://suqian.58.com/jiadian/39688091002771x.shtml
    https://suqian.58.com/jiadian/39688065683981x.shtml
    https://suqian.58.com/jiadian/39671266013200x.shtml
    https://suqian.58.com/jiadian/39658221696646x.shtml
    https://suqian.58.com/jiadian/39658199901846x.shtml
    https://suqian.58.com/jiadian/39580227892368x.shtml
    https://suqian.58.com/jiadian/39569425565066x.shtml
    https://suqian.58.com/jiadian/39569330705672x.shtml
    https://suqian.58.com/jiadian/39568930828839x.shtml
    https://suqian.58.com/jiadian/39551195806992x.shtml
    https://suqian.58.com/jiadian/39489082234641x.shtml
    https://suqian.58.com/jiadian/39447261683074x.shtml
    https://suqian.58.com/jiadian/39444944767137x.shtml
    https://suqian.58.com/jiadian/39392731060121x.shtml
    https://suqian.58.com/jiadian/39579239854613x.shtml
    https://suqian.58.com/jiadian/39557645155495x.shtml
    https://suqian.58.com/jiadian/39533918207900x.shtml
    https://suqian.58.com/jiadian/39491136867973x.shtml
    https://suqian.58.com/jiadian/39405077978014x.shtml
    https://suqian.58.com/jiadian/39389898837524x.shtml
    https://suqian.58.com/jiadian/39579201585564x.shtml
    https://suqian.58.com/jiadian/39557571197325x.shtml
    https://suqian.58.com/jiadian/39478150615072x.shtml
    https://suqian.58.com/jiadian/39456552174345x.shtml
    https://suqian.58.com/jiadian/39395190348301x.shtml
    https://suqian.58.com/jiadian/39579147037470x.shtml
'''

if __name__ == '__main__':
    get_links_from('http://suqian.58.com/bijibendiannao', 18)
    # get_item_info(channel_links)
