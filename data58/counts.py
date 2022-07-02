# encoding: utf-8
import time
from data58.page_parsing import url_list, item_info

while True:
    print(url_list.find().count())
    print(item_info.find().count())
    time.sleep(5)
