"""
def 方法名(self, 形参): 
    类里面的函数称为方法，self是表示类对象本身，
    访问成员变量的通道
def __init__(self, 形参):
    构造方法，自动运行，有构造方法可以不再单独设置变量
"""

class Student:
    name = None
    age = None
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        print(f'我叫{self.name}，今年{self.age}岁了')

stu_1 = Student(None, None)
stu_1.name = 'mike'
stu_1.age = 18
stu_1.say_hi()

stu_2 = Student('jane', 19)
stu_2.say_hi()