# encoding: utf-8
# 导入需要的模块
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# 使用函数包装，打开Chrome浏览器，选择"美食"
def get_chrome_index():
    driver = webdriver.Chrome()
    driver.get("http://www.anjuke.com")
    elem = driver.find_element_by_id("glb_search0")
    elem.clear()
    elem.send_keys("小区")
    elem.send_keys(Keys.RETURN)
    driver.close()


# 主函数
if __name__ == '__main__':
    get_chrome_index()
