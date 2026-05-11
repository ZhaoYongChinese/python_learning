import  numpy as np
import torch
from torch.utils import data
from d2l import torch as d2l
import matplotlib.pyplot as plt

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

#  读取数据
def load_array(data_arrays, batch_size, is_train=True):
    """构造一个PyTorch数据迭代器"""
    dataset = data.TensorDataset(*data_arrays)
    """
    *data_arrays: 拆包，把元组拆成多个独立的参数
    TensorDataset: 将多个张量样本按样本维度对齐，使得dataset[i]能返回对应的特征-标签对。
    """
    return data.DataLoader(dataset, batch_size, shuffle=is_train)
    # DataLoader: 负责将数据集分成小批量，并在每个epoch结束后重新打乱数据（如果shuffle=True）。
batch_size = 10
data_iter = load_array((features, labels), batch_size)

# 查看第一个批量数据
batch =next(iter(data_iter))
print(batch[0])
print(batch[1])

# 定义模型
from torch import nn

net = nn.Sequential(nn.Linear(2, 1))
# nn.Sequential: 将多个层组合成一个新的层，输入数据会依次通过这些层进行处理。
# nn.Linear(2, 1): 定义一个线性层，输入特征数为2，输出特征数为1。
net[0].weight.data.normal_(0, 0.01)
# 将线性层的权重参数初始化为均值为0、标准差为0.01的正态分布随机数。
# .normal_: 是一个原地操作方法，用于直接修改张量的数据。
net[0].bias.data.fill_(0)
# 将线性层的偏置参数初始化为0。
# .fill_: 是一个原地操作方法，用于直接修改张量的数据。

# 定义损失函数
loss = nn.MSELoss()

# 定义优化算法
trainer = torch.optim.SGD(net.parameters(), lr=0.03)
# torch.optim.SGD: 随机梯度下降优化算法，net.parameters()返回模型的所有参数，lr是学习率。

# 训练模型
num_epochs = 3
for epoch in range(num_epochs):
    for X, y in data_iter:
        l = loss(net(X), y)
        # net(X): 将输入X传入模型，得到预测值。
        # loss(net(X), y): 计算预测值与真实标签y之间的均方误差损失。
        trainer.zero_grad()
        # 在进行反向传播之前，先将梯度清零。因为PyTorch默认会累积梯度。
        l.backward()
        # 反向传播，计算损失函数关于模型参数的梯度。
        trainer.step()
        # 更新模型参数，根据计算得到的梯度进行一步优化。
    with torch.no_grad():
        # 在评估模型性能时，我们不需要计算梯度，因此使用torch.no_grad()上下文管理器来禁用梯度计算。
        train_l = loss(net(features), labels)
        # net(features): 将整个训练数据传入模型，得到预测值。
        # loss(net(features), labels): 计算整个训练数据的预测值与真实标签
        print(f'epoch {epoch + 1}, loss {float(train_l):f}')

# 训练完成后，比较学到的参数和真实参数
w = net[0].weight.data
b = net[0].bias.data
print(f'估计的w: {w.reshape(true_w.shape)}')
print(f'真实的w: {true_w}')
print(f'估计的b: {b}')
print(f'真实的b: {true_b}')
