#!/usr/bin/python
# coding:utf-8

import os
import re

import requests
import telebot

from changba import ChangBaSpider
from config import token
from quanmin import QuanMinSpider

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, '你好哇')


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(chat_id=message.chat.id, text='发送全民K歌歌曲链接即可下载歌曲')
    #bot.send_message(reply_to_message_id=message.message_id, chat_id=message.chat.id, text='发送全民K歌歌曲链接即可下载歌曲')


@bot.message_handler(commands=['prpr'])
def prpr(message):
    bot.reply_to(message=message,text='( >  < )')


@bot.message_handler(commands=['link'])
def echo(message):
    if(re.findall('http.*kg.*qq\.com\/.*',message.text)):
        link = re.findall('http.*kg.*qq\.com\/.*',message.text) #https://kg3.qq.com/node/play?s=Vd8SlgVgEjDGNVdB&shareuid=6
        songname = QuanMinSpider(link[0])
        if(songname):
            try:
                bot.send_audio(reply_to_message_id=message.message_id,chat_id=message.chat.id,audio=open(songname,'rb'))
                os.remove(songname)
            except IOError:
                print('文件被占用3')
            except FileNotFoundError:
                print('文件不存在')
        else:
            bot.send_message(reply_to_message_id=message.message_id,chat_id=message.chat.id,text='出错啦( >  < )')
    elif(re.findall('http.*changba.com\/.*',message.text)): #https://changba.com/s/FLPJaNHU6vjTJASW8xYVKg
        link = re.findall('http.*changba.com\/.*',message.text)
        songname = ChangBaSpider(link[0])
        if(songname):
            try:
                bot.send_audio(reply_to_message_id=message.message_id,chat_id=message.chat.id,audio=open(songname,'rb'))
                os.remove(songname)
            except IOError:
                print('文件被占用3')
            except FileNotFoundError:
                print('文件不存在')
        else:
            bot.send_message(reply_to_message_id=message.message_id,chat_id=message.chat.id,text='出错啦( >  < )')
    else:
       bot.send_message(reply_to_message_id=message.message_id,chat_id=message.chat.id,text='出错啦( >  < )')


@bot.message_handler()
def echo(message):
    if(re.findall('http.*kg.*qq\.com\/.*',message.text)):
        link = re.findall('http.*kg.*qq\.com\/.*',message.text) #https://kg3.qq.com/node/play?s=Vd8SlgVgEjDGNVdB&shareuid=6
        songname = QuanMinSpider(link[0])
        if(songname):
            try:
                bot.send_audio(reply_to_message_id=message.message_id,chat_id=message.chat.id,audio=open(songname,'rb'))
                os.remove(songname)
            except IOError:
                print('文件被占用3')
            except FileNotFoundError:
                print('文件不存在')
        else:
            bot.send_message(reply_to_message_id=message.message_id,chat_id=message.chat.id,text='出错啦( >  < )')
    elif(re.findall('http.*changba.com\/.*',message.text)): #https://changba.com/s/FLPJaNHU6vjTJASW8xYVKg
        link = re.findall('http.*changba.com\/.*',message.text)
        songname = ChangBaSpider(link[0])
        if(songname):
            try:
                bot.send_audio(reply_to_message_id=message.message_id,chat_id=message.chat.id,audio=open(songname,'rb'))
                os.remove(songname)
            except IOError:
                print('文件被占用3')
            except FileNotFoundError:
                print('文件不存在')
        else:
            bot.send_message(reply_to_message_id=message.message_id,chat_id=message.chat.id,text='出错啦( >  < )')

            

def asd(message=''):
    message = 'https://kg3.qq.com/node/play?s=Vd8SlgVgEjDGNVdB&shareuid=6'
    if(re.findall('http.*kg.*qq\.com\/.*',message)):
        link = re.findall('http.*kg.*qq\.com\/.*',message) #https://kg3.qq.com/node/play?s=Vd8SlgVgEjDGNVdB&shareuid=6
        songname = QuanMinSpider(link[0])
        if(songname):
            try:
                bot.send_audio(reply_to_message_id=message.message_id,chat_id=message.chat.id,audio=open(songname,'rb'))
                os.remove(songname)
            except IOError:
                print('文件被占用3')
            except FileNotFoundError:
                print('文件不存在')
        else:
            bot.send_message(reply_to_message_id=message.message_id,chat_id=message.chat.id,text='出错啦( >  < )')
    elif(re.findall('http.*changba.com\/.*',message)): #https://changba.com/s/FLPJaNHU6vjTJASW8xYVKg
        link = re.findall('http.*changba.com\/.*',message)
        songname = ChangBaSpider(link[0])
        if(songname):
            try:
                with open(songname,'rb') as data:
                    bot.send_audio(reply_to_message_id=message.message_id,chat_id=message.chat.id,audio=open(data,'rb'))
                    os.remove(data)
            except IOError:
                print('文件被占用3')
            except FileNotFoundError:
                print('文件不存在')
        else:
            bot.send_message(reply_to_message_id=message.message_id,chat_id=message.chat.id,text='出错啦( >  < )')



if __name__ == '__main__':
    bot.polling()
    #asd()