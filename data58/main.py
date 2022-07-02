# encoding: utf-8
# 导入多进程库
from multiprocessing import Pool
from data58.channel_extract_urls import channel_list
from data58.page_parsing import get_links_from


def get_all_links_from(channel):
    for num in range(1, 101):
        print(num)
        get_links_from(channel, num)


if __name__ == '__main__':
    pool = Pool()
    pool.map(get_all_links_from, channel_list.split())
