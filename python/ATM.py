storage = {
    'jane': 1000,
    'john': 500,
    'doe': 20000
}
name = input('请输入用户名：')
if name in storage:
    print('欢迎，%s！' % name)
    while True:
        print('choose your operation: 1.查询余额 2.取款 3.存款 4.退出')
        operation = input('请输入操作：')
        if operation == '1':
            print('您的余额为：%d' % storage[name])
        elif operation == '2':
            amount = float(input('请输入取款金额：'))
            if amount > storage[name]:
                print('余额不足！')
            else:
                storage[name] -= amount
                print('取款成功！您的余额为：%d' % storage[name])
        elif operation == '3':
            amount = float(input('请输入存款金额：'))
            storage[name] += amount
            print('存款成功！您的余额为：%d' % storage[name])
        elif operation == '4':
            print('退出成功！')
            break
        else:
            print('无效的操作，请重新输入！')
else:
    print('用户名不存在！')