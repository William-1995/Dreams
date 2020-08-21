# import time
# from concurrent.futures import ThreadPoolExecutor,as_completed
# from concurrent.futures import ProcessPoolExecutor

# def fib(n):
#     if n<=2:
#         return 1
#     return fib(n-1) + fib(n-2)

# def processPool():
#     with ProcessPoolExecutor(3) as executor:
#         all_tasks = [executor.submit(fib,(num)) for num in range(25,35)]
#         start_time = time.time()
#         for future in as_completed(all_tasks):
#             data = future.result()
#             print("exec result:{}".format(data))
            
#         print("last time is: {}".format(time.time() - start_time))

# if __name__ == "__main__":
#     processPool()

# import multiprocessing
# import time

# # def get_html(n):
# #     time.sleep(n)
# #     return n

# class Test:
    
#     def __init__(self):
#         pass
    
#     def t():
#         print("test")
        
#     def get_html(n):
#         time.sleep(n)
#         return n


# if __name__ == "__main__":
# #     progress = multiprocessing.Process(target=get_html,args=(2,))
# #     print(progress.pid)
# #     progress.start()
# #     progress.join()
# #     print(progress.pid)
# #     print("main progress end")
    
# #     pool = multiprocessing.Pool(multiprocessing.cpu_count())
# #     result = pool.apply_async(get_html,args=(3,))
    
# #     pool.close()
# #     pool.join() # mast be called when pool has been closed.
# #     print(result.get())
#     t = Test
#     pool = multiprocessing.Pool(multiprocessing.cpu_count())

#     # for result in pool.imap(t.get_html,[1,5,3]):
#     #     print("{} sleep success".format(result))

#     results = pool.imap_unordered(t.get_html,[1,5,3])
#     for r in results:
#         print("{} sleep success".format(r))




# import time
# from multiprocessing import Process,Queue
# from multiprocessing import Manager,Pool

# from queue import Queue
# from multiprocessing import Queue
# from multiprocessing import Manager
# Manager().Queue()

# class Pro:
#     def __init__(self):
#         pass
    
#     def producer(queue):
#         queue.put("a")
#         time.sleep(2)

#     def comsumer(queue):
#         time.sleep(2)
#         data = queue.get()
#         print(data)
    
# if __name__ == "__main__":
    # queue = Queue(10)
    # p = Pro
    # my_producer = Process(target=p.producer,args=(queue,))
    # my_consumer = Process(target=p.comsumer,args=(queue,))
    # my_producer.start()
    # my_consumer.start()
    # my_producer.join()
    # my_consumer.join()    
    #----

    # p = Pro
    # queue = Manager().Queue(10)
    # pool = Pool(2)

    # pool.apply_async(p.producer, args=(queue,))
    # pool.apply_async(p.comsumer, args=(queue,))

    # pool.close()
    # pool.join()

# import time
# from multiprocessing import Process,Queue
# from multiprocessing import Manager,Pool,Pipe

# class Pro:
#     def __init__(self):
#         pass
    
#     def producer(pipe):
#         pipe.send("Hi")
#         time.sleep(2)

#     def comsumer(pipe):
#         time.sleep(2)
#         print(pipe.recv())

# if __name__ == "__main__":
#     p = Pro
#     # Only for two process, and high performance than queue
#     recevie_pipe, send_pipe = Pipe()
#     my_producer = Process(target=p.producer,args=(recevie_pipe,))
#     my_consumer = Process(target=p.comsumer,args=(send_pipe,))

#     my_producer.start()
#     my_consumer.start()
#     my_producer.join()
#     my_consumer.join()

# from multiprocessing import Manager,Process
# def add(p_dict, key,value):
#     p_dict[key] = value

# if __name__ == "__main__" :
#     progress_dict = Manager().dict()

#     first = Process(target=add,args=(progress_dict, "age1",1))
#     second = Process(target=add,args=(progress_dict, "age2",2))
#     first.start()
#     second.start()

#     first.join()
#     second.join()
#     print(progress_dict)




# import asyncio
# import time

# async def get_html(url):
#     print("start get url")
#     await asyncio.sleep(2)
#     print("end get url")
    
# if __name__ == "__main__":
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     tasks = [get_html("http://www.baidu.com") for i in range(10)]
#     loop.run_until_complete(asyncio.wait(tasks))
#     print(time.time()-start_time)


# import asyncio
# import time
# from functools import partial

# async def get_html(url):
#     print("start get url")
#     await asyncio.sleep(2)
#     print("end get url")
#     return "willl"
    
# def callback(url, future):
#     print(url)
#     print("Send email to boby")

# if __name__ == "__main__":
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     #get_future = asyncio.ensure_future(get_html("http://www.baidu.com"))
#     tasks = loop.create_task(get_html("http://www.baidu.com"))
#     # loop.run_until_complete(get_future.result())
#     tasks.add_done_callback(partial(callback,"http://www.baidu.com"))
#     loop.run_until_complete(tasks)
#     print (tasks.result())
#     print(time.time()-start_time)


# import asyncio
# import time

# async def get_html(url):
#     print("start get url {}".format(url))
#     await asyncio.sleep(2)
#     print("end get url")
    
# if __name__ == "__main__":
#     start_time = time.time()
#     loop = asyncio.get_event_loop()
#     # tasks = [get_html("http://www.baidu.com") for i in range(10)]
#     # loop.run_until_complete(asyncio.gather(*tasks))
#     # print(time.time()-start_time)

#     # different with gather and wait
#     # gather is high-level
#     group1 = [get_html("http://www.baidu.com") for i in range(2)]
#     group2 = [get_html("http://www.kingland.com") for i in range(2)]
#     group1 = asyncio.gather(*group1)
#     group2 = asyncio.gather(*group2)

#     loop.run_until_complete(asyncio.gather(group1, group2))
#     print(time.time()-start_time)




import asyncio
import time

async def get_html(slppe_time):
    print("waiting")
    await asyncio.sleep(slppe_time)
    print("done after {}s".format(slppe_time))


if __name__ == "__main__":
    task1 = get_html(1)
    task2 = get_html(2)
    task3 = get_html(3)

    tasks = [task1,task2,task3]

    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:
        all_tasks = asyncio.Task.all_tasks()
        for task in all_tasks:
            print("cancel task")
            print(task.cancel())
        loop.stop()
        loop.run_forever()
    finally:
        loop.close()