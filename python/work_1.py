class Student():
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def check(self):
        return f'【学生姓名：{self.name}，年龄：{self.age}，地址：{self.address}】'
        

number = 10
for x in range(number):
    print(f'当前录入第{x+1}位学生信息，总共需录入{number}位学生信息')
    name = input('请输入学生姓名：')
    age = input('请输入学生年龄：')
    address = input('请输入学生地址：')
    stu_x = Student(name, age, address)
    print(f'学生{x+1}信息录入完成，信息为：{stu_x.check()}')
