"""
plt.xlim()：设置或获取x轴的范围。
plt.ylim()：设置或获取y轴的范围。
plt.xlabel()：设置x轴的标签。
plt.ylabel()：设置y轴的标签。
plt.yticks()：设置或获取y轴的刻度位置和标签。
plt.xticks()：设置或获取x轴的刻度位置和标签。
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.001, 10, 100)
y1 = np.sin(x)
y2 = np.log(x)
figure = plt.figure()
plt.plot(x, y1, x, y2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of sin(x) and ln(x)')
plt.legend(['sin(x)', 'ln(x)'])
plt.xlim(0, 10)
plt.ylim(-1, 3)
plt.show()
