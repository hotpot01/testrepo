def apply_ascyn(func,args,callback):
    result=func(*args)
    callback(result)

def add(x,y):
    return x+y

def print_result(result):
    print(result)

class ResultHandler(object):
    def __init__(self):
        self.sequence = 0

    def handle(self, result):
        self.sequence += 1
        print("[{}] Got: {}".format(self.sequence, result))