"""
plt.figure(num,figsize,dpi,FigureClass,clear,**kwargs)
num: 整数或字符串，默认值：None
    图形的编号或名称。如果提供了一个整数，它将被用作图形的编号；
    如果提供了一个字符串，它将被用作图形的名称。如果未提供，
    则使用默认编号。
figsize: 一个包含宽度和高度的元组，单位为英寸，默认值：None
    图形的宽度和高度。如果未提供，则使用默认图形大小。
dpi: 整数，默认值：None
    图形的分辨率，以每英寸点数为单位。如果未提供，则使用默认的dpi。
FigureClass: 类，默认值：None
    用于创建图形的类。如果未提供，则使用默认的Figure类。
clear: 布尔值，默认值：False
    是否在创建图形之前清除现有图形。
plot(x, y, label, linewidth, linestyle, color,
     marker, markersize, markeredgecolor, markeredgewidth,
     markerfacecolor, markerfacecoloralt, fillstyle, 
     **kwargs)
x: x轴数据
y: y轴数据
label: 字符串，图例标签。
linewidth: 数值，线条宽度。
linestyle: 字符串，线条样式，如'-'（实线）、'--'（虚线）、
    '-.'（点划线）和':'（点线）。
color: 字符串，线条颜色。
marker: 字符串，标记样式，如'o'（圆形）、's'（方形）、
    '^'（三角形）和'*'（星形）。
markersize: 数值，标记大小。
markeredgecolor: 字符串，标记边缘颜色。
markeredgewidth: 数值，标记边缘宽度。
markerfacecolor: 字符串，标记面颜色。
markerfacecoloralt: 字符串，标记面颜色的替代颜色。
fillstyle: 字符串，标记填充样式，如'full'（实心）、
    'left'（左半实心）、'right'（右半实心）和'top'（上半实心）。
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = 3 * np.ones_like(x)
figure = plt.figure(figsize=(8, 6), dpi=100)
plt.plot(x, y1, label='sin(x)', marker='o',
         markersize=5, markeredgecolor='blue',
         markeredgewidth=1, markerfacecolor='cyan',
         fillstyle='full')
plt.plot(x, y2, label='y=3', color='red', linestyle='--')
plt.legend()  # 显示图例
plt.show()
