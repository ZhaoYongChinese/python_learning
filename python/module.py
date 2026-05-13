"""
from module import function: 从模块导入函数
from module import *: 从模块导入所有函数
*表示导入模块中的所有函数，但不推荐使用，因为它可能会导致命名冲突
*如果模块中有__all__变量，*将只导入__all__中列出的函数
import module: 导入整个模块
import module as alias: 导入模块并给它一个别名
from module import function as alias: 从模块导入函数并给它一个别名
"""
