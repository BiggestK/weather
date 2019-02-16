#-*-coding: utf-8 -*-
# @Time : 2018/4/16  21:01
# @Author: BigK
#用bs4 网页分析

from bs4 import BeautifulSoup
import requests
import time
import json
import sys


Comprehensive_List = []
City_list = []
Wend_list = []
Weather_list = []
Max_list = []
Min_list = []

from echarts import Echart,Bar,Axis
def get_weather(url):
    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.168 Safari/537.36',
    'Upgrade-Insecure-Requests':'1',
    'Referer':'http://www.weather.com.cn/textFC/db.shtml',
    'Host':'www.weather.com.cn'
}

    req = requests.get(url,headers = headers)

#content返回二进制，text返回unicode
#print (unicode(req.content,encoding = "utf-8"))

#所有城市都是放在属于某个直辖市或省的表格中
#真正有用的数据是从第2个tr开始的（下标是0）
#真正有用的第0个tr中的第0个td，表示的是省份名称
#其余tr的第0个td表示城市的名字
    content = req.content
    soup = BeautifulSoup(content,'lxml')
    conMidtab = soup.find('div',class_= 'conMidtab')
    conMidtab2_list = conMidtab.find_all('div',class_='conMidtab2')
    for x in conMidtab2_list:
        tr_list = x.find_all('tr')[2:]  #把前两个tr去掉
        #如果是第0个tr标签，城市名是和省份名称放在一起的
        #如果不是，那么这个tr标签中只存放城市名
        for index,tr in enumerate(tr_list):
            min = max = 0
            if index == 0:
                td_list = tr.find_all('td')
                province = td_list[0].text.replace('\n','')
                city = td_list[1].text.replace('\n','')
                weather = wend = td_list[2].text.replace('\n','')
                wend = td_list[3].text.replace('\n','')
                max = td_list[4].text.replace('\n','')
                min = td_list[7].text.replace('\n','')
            else:
                td_list = tr.find_all('td')
                city = td_list[0].text.replace('\n','')
                weather = td_list[1].text.replace('\n', '')
                wend = td_list[2].text.replace('\n', '')
                max = td_list[3].text.replace('\n', '')
                min = td_list[6].text.replace('\n', '')
            print('%s | %s | %s | max:%s °C | min:%s°C'% ((province + city),weather,wend,max,min))

            Comprehensive_List.append({
                'City':province + city,
                'Weather':weather,
                'Wend':wend,
                'Max':max,
                'Min':min
            })
            City_list.append(province + city)

            Weather_list.append(weather)

            Wend_list.append(wend)

            Max_list.append(max)

            Min_list.append(min)

def main():
    urls = ['http://www.weather.com.cn/textFC/hb.shtml',
            'http://www.weather.com.cn/textFC/db.shtml',
            'http://www.weather.com.cn/textFC/hd.shtml',
            'http://www.weather.com.cn/textFC/hz.shtml',
            'http://www.weather.com.cn/textFC/hn.shtml',
            'http://www.weather.com.cn/textFC/xb.shtml',
            'http://www.weather.com.cn/textFC/xn.shtml',
    ]
    for url in urls:
        get_weather(url)
        time.sleep(3)

    line = json.dumps(Comprehensive_List,ensure_ascii=False)
    with open('comprehensive3.json','w') as fp:
        fp.write(line)


if __name__ == '__main__':
    main()
