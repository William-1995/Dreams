from multiprocessing import Pool

from multiprocessing import cpu_count

import gevent
def test1(i):
    print (12)
    gevent.sleep(i)
    print (34)
def test2(i):
    print (56)
    gevent.sleep(i)
    print (78)
def coroutine():
    gevent.joinall([
        gevent.spawn(test1),
        gevent.spawn(test2)
    ])
if __name__=="__main__":
    p=Pool()
    for i in range(3):
        p.apply_async(coroutine,args=(i,))
    p.close()