#-*-coding: utf-8 -*-
# @Time : 2018/4/17  11:25l'l'l'l'l'l'l'l'l'l'l'l'l'l
# @Author: BigK
import json
list = []
def main():

    f = open('PM2.5555.json')
    data = ''
    for line in f:
        data += line
    dic={}

    s = json.loads(data)
    for i in range(0,357):
        #print(s[i]['Rank']+" ",end="")

        a = s[i]['City']
        dic = {a:[s[i]['AOI']]}
        dic[a].append(s[i]['PM'])
        list.append('{'+'name: '+'"'+a.rstrip('市')+'"'+','+'value: '+'['+s[i]['AOI']+', '+s[i]['PM'].rstrip('μg/m³')+']'+'}'+',')
        #print('{'+'name: '+'"'+a+'"'+','+'value: '+'['+s[i]['AOI']+', '+s[i]['PM'].rstrip('μg/m³')+', '+'\''+s[i]['Level']+'\''+']'+'}'+',')
        print('\''+a+'\''+',',end = '')
with open("data1.txt", "w") as f:
    for i in list:
        f.write(list)
    #     list.append(s[i]['City'])
    # print(list)
        #print(s[i]['PM'])

if __name__ == '__main__':
    main()