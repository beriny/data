# encoding: utf-8
# import sys

def read_file():
    f = open("hello.txt", "r")
    for line in f.readlines():
        print(line.strip())
    f.close()


if __name__ == '__main__':
    read_file()
