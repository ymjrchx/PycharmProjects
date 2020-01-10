# coding=utf-8
import _thread
import time


def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())))

try:
    _thread.start_new_thread(print_time,("thread-1",2,))
    _thread.start_new_thread(print_time,("thread -2",2,))
except:
    print("Error: 无法启动线程")
if __name__ == '__main__':
    pass
