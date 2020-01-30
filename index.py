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
    print '日期: ' + item['date'].encode('utf-8') + ', '\
        + '已确诊: ' + item['cn_conNum'].encode('utf-8') + ', '\
        + '疑似: ' + sus.encode('utf-8') + ', '\
        + '死亡: ' + item['cn_deathNum'].encode('utf-8') + ', '\
        + '治愈: ' + item['cn_cureNum'].encode('utf-8')
# print json.dumps(data, encoding="utf-8", ensure_ascii=False)
# print(r.headers)
# print(r.encoding)
# print(r.content)
        