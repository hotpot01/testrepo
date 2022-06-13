#可以保存执行的上下文，从中断的地方继续执行
#生产者，消费者模型，需要通过循环来模拟

def consumer():
    r= yield ''
    while True:
        #这里，r的值不断被接收，不断被返回
        r=yield r
#要一边生产一边消费
def producer(c):
    #send就算是生产了
    #初始化
    c.send(None)
    n=0
    while n<5:
        n = n + 1
        print('produce %d'%n)
        #消费者return回来的数据需要重新赋值
        r=c.send(n)
        print('consume %d'% r)
    c.close()

c=consumer()
producer(c)