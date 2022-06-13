from xmlrpc.server import SimpleXMLRPCServer

class cal():
    def add(self,x,y):
        return x+y
    def multi(self,x,y):
        return x*y
    def sub(self,x,y):
        return x-y
    def div(self,x,y):
        return x/y

obj=cal()
server=SimpleXMLRPCServer(('localhost',8088))
server.register_instance(obj)
server.register_multicall_functions()
server.register_function()
server.serve_forever()