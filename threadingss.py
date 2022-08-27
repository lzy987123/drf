# """
#     多线程执行
# """
# import datetime
# from time import sleep
# import threading
# import sys, getopt
#
# class Test(threading.Thread):
#
#     # TODO 初始化参数
#     def __init__(self, times):
#         threading.Thread.__init__(self)
#         self.times = times
#
#     # TODO 逻辑代码
#     def run(self):
#         print('time is %s start: %s' % (self.times, str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))))
#         sleep(3)
#         print('time is %s start: %s' % (self.times, str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))))
#         sleep(3)
#
#
#     # TODO 资源回收
#     def __del__(self):
#         print('over %s' % self.times)
#
# def run():
#     mythreads = []
#     # 线程数设置
#     lites = 5
#     # 创建多线程
#     for item in range(lites):
#         try:
#             task_item = Test(item)
#             task_item.start()
#             mythreads.append(task_item)
#         except:
#             raise
#
#     for thread in mythreads:
#         thread.join()
#
# if __name__ == '__main__':
#     run()


import threading


def thread_job():
    print('线程ID %s' % threading.current_thread())


def main():
    added_thread = threading.Thread(target=thread_job)  # 创建线程
    added_thread.start()  # 启动线程


if __name__ == '__main__':
    main()

