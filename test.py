def test_return():
    return 1,2
a = test_return()
c,d = test_return()
print(c,type(c))  # 输出: 1 <class 'int'>
print(d,type(d))  # 输出: 2 <class 'int'>
print(a,type(a))  # 输出: (1, 2)