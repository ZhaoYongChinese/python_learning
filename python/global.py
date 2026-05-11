a = 3
def number():
    global a # 声明a为全局变量
    a = 5
    print(a)
number()
print(a)