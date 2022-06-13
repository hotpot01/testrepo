#整体的逻辑是
#把一个generator标记为协程类型，然后利用yield from 语句 调用另一个协程
#可以用语法改造下
# async await
#同步会有10s的执行，异步只需要5s,切出去执行的时间，也相当于同时在执行了（单线程并发操作）
import asyncio
import time
async def hello():
    a=time.time()
    print('hello world')
    r=await asyncio.sleep(5)
    print('hello again')
    b=time.time()
    print(b-a)
c=time.time()
loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([hello(),hello()]))
loop.close()
d=time.time()
print(d-c)