#-*-coding: utf-8 -*-
# @Time : 2018/4/18  14:41
# @Author: BigK
import json
from urllib.request import urlopen, quote
list=[]
a=[]
dic ={}
url = 'http://api.map.baidu.com/geocoder/v2/'
output = 'json'
ak = '6mkjChy6GDiOv1xhzmjEK1qx4wLuDTN8'

a = ['北京', '天津', '石家庄', '太原', '呼和浩特', '沈阳', '大连', '长春', '哈尔滨', '上海', '南京', '杭州', '宁波', '合肥', '福州', '厦门', '南昌', '济南',
     '青岛', '郑州', '武汉', '长沙', '广州', '深圳', '南宁', '海口', '重庆', '成都', '贵阳', '昆明', '拉萨', '西安', '德宏州','兰州', '西宁', '银川', '乌鲁木齐',
     '青岛','苏州','南通','赤峰','宜兴','连云港','乌镇']
# f = open('PM2.5.json')
# data = ''
# for line in f:
#     data += line
#
# s = json.loads(data)
# for i in range(0, 365):
# # print(s[i]['Rank']+" ",end="")
#     list.append(s[i]['City'])
# a = list

for i in a:
    add = quote(i)
    uri = url + '?' + 'address=' + add + '&output=' + output + '&ak=' + ak  # 百度地理编码API
    req = urlopen(uri)
    res = req.read().decode()
    temp = json.loads(res)
    dic[i] = temp['result']['location']['lng'], temp['result']['location']['lat']
    #print(i,temp['result']['location']['lng'], temp['result']['location']['lat'])  # 打印出经纬度
print (dic)