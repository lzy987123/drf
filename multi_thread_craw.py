import threading
import time

import blog_spider


def multi_thread():
	print("multi_thread begin")
	threads =[]
	for url in blog_spider.urls:
		threads.append(
			threading.Thread(target=blog_spider.craw, args=(url,))
		)
	for thread in threads:
		thread.start()
	for thread in threads:
		thread.join()

	print("multi_thread end")

if __name__ == '__main__':
	create_time = time.time()
	multi_thread()
	end_time = time.time()
	print(end_time - create_time)
