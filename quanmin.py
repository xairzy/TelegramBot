#!/usr/bin/python
# coding:utf-8

import telebot
import requests
import re
import os

def QuanMinSpider(link=''):
    html = requests.get(link)
    text = html.content.decode('utf-8')
    result = re.findall('"playurl":"(http://.*\.m4a[\w=&?]*)"', text) #()代表list[0]
    if(result):
        try:
            title = re.findall('"song_name":"(.*?)"',text)
            songer = re.findall('"nick":"(.*?)"',text)
            stra = re.findall('\[\/em\](.*)',songer[0]) #去掉表情名字
            if(stra):
                songer[0] = stra[0]
            r=requests.get(result[0])
            filesong = requests.get(url = result[0])
            songname = title[0]+'-'+songer[0]+'.m4a'
            with open(songname , 'wb') as fp:
                try:
                    fp.write(filesong.content)
                except FileNotFoundError:
                    print('文件不存在')
                except IOError:
                    print('文件被占用1')
            return songname
        except:
            return ''


if __name__ == '__main__':
    QuanMinSpider()