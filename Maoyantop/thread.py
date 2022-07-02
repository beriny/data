#! /usr/bin/py
# coding=utf-8

import threading
import time
from subprocess import Popen, PIPE


def ping_check(ip):
    check = Popen(['/bin/bash', '-c', 'ping -c 2' + ip], stdin=PIPE, stdout=PIPE)
    data = check.stdout.read()
    if 'ttl' in data:
        print('%s is UP' % ip)


def main():
    threads = []
    for i in range(1, 255):
        ip = '106.42.25.' + str(i)
        for thread in threads:
            thread += 1
            thread = threading.Thread(target=ping_check)
            thread.setDaemon(True)
            threads.join(thread)
            thread.start(ip)
            time.sleep(0.1)
            print(thread)


if __name__ == '__main__':
    main()
