import zerorpc

class cal(object):
    def add(self,x,y):
        return x+y
    def multi(self,x,y):
        return x*y
    def sub(self,x,y):
        return x-y
    def div(self,x,y):
        return x/y

s=zerorpc.Server(cal())
s.bind("tcp://0.0.0.0:4243")
s.run()