# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import json
target = 'https://interface.sina.cn/news/wap/fymap2020_data.d.json'
r = requests.get(target)
r.encoding = r.apparent_encoding
# print(r.status_code)
data = r.text.encode('utf-8')
# data = r.text
# data = r.json()
historylist = json.loads(data).get('data').get('historylist')
for item in historylist:
    sus = item['cn_susNum']
    if sus is None:
        sus = u'0'
    # print 'date: ' + item['date'].encode('utf-8') + ', '\
    #     + 'gntotal: ' + item['cn_conNum'].encode('utf-8') + ', '\
    #     + 'sustotal: ' + sus.encode('utf-8') + ', '\
    #     + 'deathtotal: ' + item['cn_deathNum'].encode('utf-8') + ', '\
    #     + 'curetotal: ' + item['cn_cureNum'].encode('utf-8')

dates = [i['date'].encode('utf-8') for i in historylist]
gntotal = [i['cn_conNum'].encode('utf-8') for i in historylist]

dates.reverse()
gntotal.reverse()



#
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# x = ["01.11","01.12","01.13","01.14","01.15","01.16","01.17"]
# y1 = [1, 2, 3, 4, 5, 6, 7]
# y2 = [3, 5, 7, 1, 6, 7, 2]
plt.figure(figsize=(15,8), dpi=80)
plt.plot(dates, gntotal, label="adsf")
# plt.plot(x, y2, label="asdfsadf")
plt.title(u"Analysis")
plt.legend()
plt.show()

# print json.dumps(data, encoding="utf-8", ensure_ascii=False)
# print(r.headers)
# print(r.encoding)
# print(r.content)
        