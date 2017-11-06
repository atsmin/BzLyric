# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

ARTIST_ID = 'a00067d'  # B'z
BASE_URL = 'http://j-lyric.net'
LYRIC_LIST_URL = BASE_URL + '/artist/' + ARTIST_ID

with open('./urls.txt', 'w') as f:
    r = requests.get(LYRIC_LIST_URL)
    soup = BeautifulSoup(r.content, 'html.parser')

    divs = soup.find_all('div', id=re.compile('^ly'))
    ps = [div.find_all('p', class_='ttl')[0] for div in divs]
    urls = [BASE_URL + p.find_all('a')[0]['href'] for p in ps]

    f.write('\n'.join(urls))
