
#类方法，实例方法，静态方法
#继承

class Stu():
    _stu=0
    @classmethod
    def howmany(cls):
        print(Stu._stu)
    def __init__(self,name,gender):
        Stu._stu+=1
        self.name=name
        self.gender=gender
    def hellostu(self):
        if self.gender==1:
            print('hello little boy:{}'.format(self.name))
        if self.gender==0:
            print('hello little gril{}'.format(self.name))