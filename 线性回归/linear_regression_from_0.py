import random
import torch
import numpy as np
from d2l import torch as d2l
import matplotlib.pyplot as plt
import time



# 生成数据集
def synthetic_data(w, b, num_examples):
    """生成y=Xw+b+噪声"""
    X = torch.normal(0,1,(num_examples, len(w)))
    y = torch.matmul(X,w)+b
    y += torch.normal(0, 0.01, y.shape)
    return X, y
true_w = torch.tensor([[2], [-3.4]])
true_b = 4.2
features, labels = synthetic_data(true_w, true_b, 1000)

# 可视化数据集
# plt.figure()

# plt.scatter(features[:, 0].detach().numpy(), labels.detach().numpy(), 5)
# plt.xlabel('Feature 0')
# plt.ylabel('Label')
# plt.title('Feature 0 vs Label')

# plt.figure()
# plt.scatter(features[:, 1].detach().numpy(), labels.detach().numpy(), 5)
# plt.xlabel('Feature 1')
# plt.ylabel('Label')
# plt.title('Feature 1 vs Label')

# plt.show()

# 读取数据
def data_iter(batch_size, features, labels):
    num_examples = len(features)
    indices = list(range(num_examples))
    random.shuffle(indices)  # 样本的读取顺序是随机的
    for i in range(0, num_examples, batch_size):
        batch_indices = torch.tensor(
            indices[i: min(i + batch_size, num_examples)])
        # 通过yield生成一个迭代器对象，后续每次调用next()都会返回一个新的批量数据
        yield features[batch_indices], labels[batch_indices]

# 设置批量大小
batch_size = 10

# 初始化模型参数
w = torch.normal(0, 0.01, size=(2, 1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)

# 定义模型
def linreg(X, w, b):
    """线性回归模型"""
    return torch.matmul(X, w) + b

# 定义损失函数
def squared_loss(y_hat, y):
    """均方损失"""
    return (y_hat - y.reshape(y_hat.shape)) ** 2 / 2

# 定义优化算法
def sgd(params, lr, batch_size):
    """小批量随机梯度下降"""
    with torch.no_grad():
        for param in params:
            param -= lr * param.grad / batch_size
            param.grad.zero_()

# 开始计时
start_time = time.time()

# 训练模型
lr = 0.03
num_epochs = 3
net = linreg
loss = squared_loss
for epoch in range(num_epochs):
    for X, y in data_iter(batch_size, features, labels):
        l = loss(net(X, w, b), y)  # 计算损失
        l.sum().backward()  # 小批量的损失的和进行反向传播
        sgd([w, b], lr, batch_size)  # 使用参数的梯度更新参数
    with torch.no_grad():
        train_l = loss(net(features, w, b), labels)
        print(f'epoch {epoch + 1}, loss {float(train_l.mean()):f}')

# 训练完成后，比较学到的参数和真实参数
print(f'估计的w: {w.reshape(true_w.shape)}')
print(f'真实的w: {true_w}')
print(f'估计的b: {b}')
print(f'真实的b: {true_b}')

# 结束计时
end_time = time.time()
print(f'训练时间: {end_time - start_time:.2f} seconds')