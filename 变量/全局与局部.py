
count=0
def infunc():
    import random
    print(random.randint(1,10))
def change(num):
    global count
    count=num
    print(count)

if __name__ == '__main__':
    infunc()
    #未全局引用
    #random.randint(1, 10)
    change(6)
    print(count)