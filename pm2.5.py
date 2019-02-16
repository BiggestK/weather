#-*-coding: utf-8 -*-
# @Time : 2018/4/18  15:29
# @Author: BigK
import requests
from bs4 import BeautifulSoup
import json

Atmosphere_List = []
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.168 Safari/537.36',
    'Upgrade-Insecure-Requests':'1',
    'Referer':'http://www.86pm25.com/city/anshan.html',
    'Host':'www.86pm25.com'
}
url = 'http://www.86pm25.com/paiming.htm'
req = requests.get(url,headers = headers)
#
content = req.content
soup = BeautifulSoup(content,'lxml')
weilai = soup.find('div',class_= 'weilai')
trs = weilai.find_all('tr')[1:]


for x in trs:
    tds = x.find_all('td')
    rank = tds[0].text
    city = tds[1].text.rstrip('市区地')
    aqi = tds[3].text
    level = tds[4].text
    pm = tds[5].text.rstrip('μg/m³')
    print('排名:%s  | %s | 空气质量指数：%s | 空气质量: %s| pm2.5:%s' % (rank, city, aqi , level , pm))
    Atmosphere_List.append({
        'Rank': rank,
        'City': city,
        'AOI': aqi,
        'Level': level,
        'PM': pm
})
line = json.dumps(Atmosphere_List)
with open('PM2.55555.json', 'w') as fp:
    fp.write(line)

    # for y in tds:
    #     divs = y.find_all('div')
    #     print (divs)
        # for i in range (len(divs)):
        #     if i%6-1 == 0 or i%6-5 == 0:

