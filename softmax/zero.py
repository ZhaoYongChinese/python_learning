import torch
import torchvision
from torch.utils import data
from torchvision import transforms
from d2l import torch as d2l
import os

# torchvision: 是一个PyTorch的官方库，
# 提供了常用的计算机视觉数据集、模型和图像变换工具。
# transforms: 是torchvision中的一个模块，
# 提供了常用的图像变换操作，如裁剪、缩放、旋转等。
# d2l: 是《动手学深度学习》一书的配套库，
# 提供了许多实用的工具函数和类，简化了深度学习的实现过程。

d2l.use_svg_display()
# use_svg_display: 是d2l库中的一个函数，
# 用于设置Matplotlib的图形显示为SVG格式，这样可以获得更清晰的图像。

# 读取数据
path = os.getcwd()
# os.getcwd(): 获取当前工作目录的路径。
trans = transforms.ToTensor()
mnist_train = torchvision.datasets.FashionMNIST(
    root=os.path.join(path, "data"), train=True, 
    transform=trans,download=True)
mnist_test = torchvision.datasets.FashionMNIST(
    root=os.path.join(path, "data"), train=False, 
    transform=trans,download=True)
# torchvision.datasets.FashionMNIST: 
# 是torchvision库中提供的一个数据集类，
# 用于加载Fashion-MNIST数据集。它接受几个参数：
# root: 数据集的根目录路径。
# train: 布尔值，指定是否加载训练集。
# transform: 对数据进行预处理的变换操作。
# 通过os.path.join()函数将当前工作目录路径与"data"字符串连接起来，
# 构成数据集的根目录路径,确保数据集被正确存储在该目录下。
# 通过设置transform=trans，将数据转换为PyTorch张量格式。
# 通过设置download=True，如果数据集不存在于指定的根目录下，
# 则会自动下载数据集。

# 可视化数据集
def get_fashion_mnist_labels(labels):
    """返回Fashion-MNIST数据集的文本标签"""
    text_labels = ['t-shirt', 'trouser', 'pullover', 'dress', 'coat',
                   'sandal', 'shirt', 'sneaker', 'bag', 'ankle boot']
    return [text_labels[int(i)] for i in labels]

# 获取前面几个数据样本的文本标签
def show_images(imgs, num_rows, num_cols, titles=None, 
                scale=1.5):
    """Plot a list of images."""
    figsize = (num_cols * scale, num_rows * scale)
    _, axes = d2l.plt.subplots(num_rows, num_cols, 
                               figsize=figsize)
    axes = axes.flatten()
    for i, (ax, img) in enumerate(zip(axes, imgs)):
        if torch.is_tensor(img):
            # 图片张量
            ax.imshow(img.numpy())
        else:
            # PIL图片
            ax.imshow(img)
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        if titles:
            ax.set_title(titles[i])
    return axes