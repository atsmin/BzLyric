# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

DIR = './lyrics'

with open('./urls.txt', 'r') as f:
    for url in f:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')

        title = soup.find_all('h2')[0].text
        title = re.sub('^\'', '', title)
        title = re.sub('^\"', '', title)
        title = re.sub('\'$', '', title)
        title = re.sub('\"$', '', title)
        title = title.replace(' 歌詞', '').strip()
        print(title)

        lyric = '\n'.join([x for x in soup.find(id='Lyric').stripped_strings if len(x) > 0])
        lyric = lyric.replace('<br/>', '。').replace('(※くり返し)', '').replace('(△くり返し)', '').replace('※', '').replace('△', '')
        lyric = lyric.strip()
        with open(DIR + '/' + title, 'w') as f2:
            f2.write(lyric)

