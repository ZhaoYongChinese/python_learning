a = 10.51
b = int(a)      # 直接截断小数部分，得到10
c = round(a)    # round函数四舍五入，舍[0,0.5]向下，入(0.5,1)向上
d = round(a, 1) # round函数可以指定小数位数，这里保留1位小数，得到10.5
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)