# list = [1,2,3]
# -*- coding: utf-8 -*-
# import matplotlib.pyplot as plt
# import matplotlib as mpl
import numpy as np
# x1 = ["01.11","01.12","01.13","01.14","01.15","01.16","01.17","01.18","01.19","01.20","01.21","01.22","01.23","01.24","01.25","01.26","01.27","01.28","01.29"]
# y1 = ["41","41","41","41","41","45","62","121","198","258","440","571","830","1287","1975","2744","4515","5974","7736"]
# y2 = ["0","0","0","0","0","0","0","0","0","54","91","348","1072","1965","2684","5794","6973","9239","12167"]
# # y3 = ["1","1","1","1","1","2","2","3","4","6","9","17","25","41","56","80","106","132","170"]
# # y4 = ["2","6","7","7","7","7","19","24","25","25","25","30","34","38","49","51","60","103","124"]
# plt.figure(figsize=(16,7))
# # plt.title("ABC")
# plt.plot(x1,y1,label="conNum", linewidth=2, color='b', marker='o',markerfacecolor='blue', markersize=6)
# plt.plot(x1,y2,label="susNum", linewidth=2, color='y', marker='o',markerfacecolor='yellow', markersize=6)
# # plt.ylabel("number")
# for a, b in zip(x1,y1):
#     plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
# for c, d in zip(x1,y2):
#     plt.text(c, d, d, ha='center', va='bottom', fontsize=10)
#x_axix，train_pn_dis这些都是长度相同的list()
# # sub_axix = filter(lambda x:x%200 == 0, x_axix)
# plt.plot(x_axix, train_acys, color='green', label='training accuracy')
# plt.plot(sub_axix, test_acys, color='red', label='testing accuracy')
# plt.plot(x_axix, train_pn_dis,  color='skyblue', label='PN distance')
# plt.plot(x_axix, thresholds, color='blue', label='threshold')
from matplotlib import pyplot as plt
from matplotlib import font_manager
x = ["01.11","01.12","01.13","01.14","01.15","01.16","01.17","01.18","01.19","01.20","01.21","01.22","01.23","01.24","01.25","01.26","01.27","01.28","01.29"]
y1 = ["41","41","41","41","41","45","62","121","198","258","440","571","830","1287","1975","2744","4515","5974","7736"]
y2 = ["0","0","0","0","0","0","0","0","0","54","91","348","1072","1965","2684","5794","6973","9239","12167"]
plt.figure(figsize=(15,8), dpi=80)
plt.plot(x,y1,label="conNum", linewidth=2, color='b', marker='o',markerfacecolor='blue', markersize=6)
plt.plot(x,y2,label="susNum", linewidth=2, color='y', marker='o',markerfacecolor='yellow', markersize=6)


plt.legend()
plt.show()

