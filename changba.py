#!/usr/bin/python
# coding:utf-8

import telebot
import requests
import re
import os

def ChangBaSpider(link=''):
    html = requests.get(link)
    text = html.content.decode('utf-8')
    result = re.findall('var.a="(http.*)",',text)
    if(result):
        try:
            songmessage = re.findall('<title>(.*)</title>',text)
            songer = re.findall('-\s+(.*)',songmessage[0][0:-11])
            songname = re.findall('(.*)\s+-',songmessage[0][0:-11])
            newsongname = songname[0] + '-'+ songer[0] +'.mp3'
            r=requests.get(result[0])
            filesong = requests.get(url = result[0])
            with open(newsongname, 'wb') as fp:
                try:
                    fp.write(filesong.content)
                except FileNotFoundError:
                    print('文件不存在')
                except IOError:
                    print('文件被占用1')
            return newsongname
        except:
            return ''


   

if __name__ == '__main__':
    ChangBaSpider()


