# import asyncio

# def callback(sleep_times, loop):
#     print("success. time:{}".format(loop.time()))

# def stoploop(loop):
#     loop.stop()
    
# #call_later, call_at, call_soon
# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     now = loop.time()
#     loop.call_at(now+2, callback,2, loop)
#     loop.call_at(now + 1, callback,1, loop)
#     loop.call_at(now + 3, callback,3, loop)
#     loop.call_soon(callback, 4, loop)
#     # loop.call_soon(stoploop,loop)
#     loop.run_forever()


import time
import asyncio
from concurrent.futures import ThreadPoolExecutor

def get_url(url):
    time.sleep(2)

if __name__ == "__main__":
    import time
    start_time = time.time()
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor(3)
    tasks = []
    for url in range(20):
        url = "http://www.baidu.com"
        task = loop.run_in_executor(executor, get_url, url)
        tasks.append(task)
    loop.run_until_complete(asyncio.wait(tasks))
    print("last time:{}".format(time.time() - start_time))