#asyncio,
#把协程放回eventloop中
#这些异步的操作，只针对协程，放回eventbus中执行的数据要求需要是协程

#一个疑问，为啥两个loop执行的时候会失效，因为一个py只有一个线程？？
#需要重新分配一个loop
import asyncio
import  threading

#定义数据
@asyncio.coroutine
#把一个genertor标记为协程类型，用yield返回的就是genertor
def hello():
    print('hello world')
    #asyncio.sleep(1),也是一个协程，
    r=yield from(asyncio.sleep(1))
    print(r)
    print('hello again')

#获取eventloop
loop=asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()


#可以用Task分装多个协程，然后也是同一个线程执行的
#写起来会多一点东西

@asyncio.coroutine
#把一个genertor标记为协程类型，用yield返回的就是genertor
def helloone():
    print('hello world (%s)' % threading.currentThread())
    #asyncio.sleep(1),也是一个协程，
    r=yield from(asyncio.sleep(1))
    print(r)
    print('hello again (%s)' % threading.currentThread())

loopone=asyncio.get_event_loop()
tasks=[helloone(),helloone()]
loopone.run_until_complete(asyncio.wait(tasks))
loopone.close()