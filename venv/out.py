#-*-coding: utf-8 -*-
# @Time : 2018/4/20  14:27
# @Author: BigK
import json
list = []
def main():

    f = open('out.txt')
    data = ''
    for line in f:
        data += line


    for i in range(0,15600):
        #print(s[i]['Rank']+" ",end="")

        list.append(s[i][1])
    print(list)
        #print(s[i]['PM'])

if __name__ == '__main__':
    main()