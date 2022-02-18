import discord
import requests
import json
from bs4 import BeautifulSoup
import urllib
import urllib.request
from urllib.request import urlopen, Request
import html.parser
from socket import error as SocketError
from http.cookiejar import CookieJar
import re
import os
# connection to discord
client = discord.Client()

def crawl():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    cj = CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    req = Request(url="https://leetcode.com/problemset/all/?difficulty=EASY&page=2",headers=headers)
    response = opener.open(req).read()

    soup = BeautifulSoup(response, "lxml")

    links = []
    for link in soup.findAll('a'):
        print("{0} link: leetcode.com{1}".format(link.text.strip(),link.get('href')))

    print(links)
    # for id in response:
        # print("id: {}",id)
    # print(response)

def get_link():
    response = requests.get("https://leetcode.com/api/problems/all/")
    
    with open('https://leetcode.com/problemset/all/?difficulty=EASY&page=1', 'r') as html_file:
        content = html_file.read()
        print(content)
    # print(json_data)

# registering an event
@client.event
async def on_ready():
    # when the bot is ready to use
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        get_link()
        await message.channel.send('Hello!')
    # if message.content.startswith('$leetcode'):
    #     await message.channel.send(get_link()[:400])

# line to run the bot
# client.run("OTQyMjQ0NzI5OTA5ODMzNzU4.YghryQ.Qb1-YGbzTDbgQnNVBqmFHMEv5PM")
crawl()