# -*- coding: utf-8 -*-
# import matplotlib.pyplot as plt
# import matplotlib as mpl
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
x = ["01.11","01.12","01.13","01.14","01.15","01.16","01.17"]
y1 = [1, 2, 3, 4, 5, 6, 7]
y2 = [3, 5, 7, 1, 6, 7, 2]
plt.figure(figsize=(15,8), dpi=80)
plt.plot(x, y1, label="adsf")
plt.plot(x, y2, label="asdfsadf")
plt.title(u"原始数据分布")
plt.legend()
plt.show()