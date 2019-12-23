#!/usr/bin/python

from bs4 import BeautifulSoup as bs
import requests

import click
import os
from pprint import pprint





SEARCH_URL = 'https://www.pornhub.com/video/search?search='
BASE_URL = 'https://www.pornhub.com'

@click.command()
@click.option('--search')
@click.option('--count', default=5)

def search(search):
    req = requests.get(SEARCH_URL + search).content
    soup = bs(req, 'html.parser')

    list_items = soup.find_all('a', class_='linkVideoThumb js-linkVideoThumb img')

    video_list = []
    for item in list_items:
        video_list.append(
            {
                'title': item.find('img')['alt'],
                'video-url': BASE_URL + item['href'],
                'thumb-url': item.find('img')['src']
            }
        )

    num = 1
    for item in video_list:
        print(str(num) + ' - ' + item.get('title'))
        num += 1

if __name__ == '__main__':
    search()