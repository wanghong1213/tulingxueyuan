'''
利用time函数，生成两个函数
顺序调用
计算总的运行时间

# 案例02： 改用多线程，缩短总时间，使用_thread
'''

import time
import _thread as thread


def loop1():
    # ctime 得到当前时间
    print('Start loop 1 at :', time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(4)
    print('End loop 1 at:', time.ctime())


def loop2():
    # ctime 得到当前时间
    print('Start loop 2 at :', time.ctime())
    # 睡眠多长时间，单位是秒
    time.sleep(2)
    print('End loop 2 at:', time.ctime())


def main():
    print("starting at:", time.ctime())
    # 启用多线程的意思是用多线程去执行某个函数
    # 启用多线程函数为start_new_thead
    # 参数两个,一个式需要运行函数名,第二式函数的参数作为元祖使用,为空则使用空元祖
    # 注意:如果函数只有一个参数,需要参数后由一个逗号

    thread.start_new_thread(loop1,())
    thread.start_new_thread(loop2,())

    print("All done at:", time.ctime())


if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)






