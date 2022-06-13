#asyncio，这个分装了各种协程式处理的函数，TCP，UDP，SSL协议处理，aiohttp会对asyncio进行分装处理
#主要还是服务端性能对处理，性能的上下限；理论上所有的请求都可以在一个IO时间中完成
#这里还需要对网络编程了解,返回请求头和请求体，响应头和响应体
import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s host' % host)
    #建立异步对链接（协程实现）
    connect=asyncio.open_connection(host,80)
    #这里也很底层了吧，建立链接之后，还要进行处理，发送请求
    reader,writer=yield from connect
    header='GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    #这一块是什么逻辑?
    #应该是生产者，建立链接后，服务器返回的数据都写回通道里面去
    yield from writer.drain()
    while True:
        line=yield from reader.readline()
        if line==b'\r\n':
            break
        print('%s header > %s'%(host,line.decode('utf-8').rstrip()))
    writer.close()

loop=asyncio.get_event_loop()
tasks=[wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()