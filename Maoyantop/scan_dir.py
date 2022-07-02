# encoding: utf-8
import sys
import requests

url = sys.argv[1]
def scan_directory():
    with open("hello.txt", "r") as f:
        for line in f.readlines():
            line = line.strip()
            print(line)
            wb_data = requests.get(url + line)
            if wb_data.status_code == 200:
                print("url:" + wb_data.url + "exist"

# if __name__ == '__main__':
scan_directory()
