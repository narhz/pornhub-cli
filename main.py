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

def search(search, count):
    req = requests.get(SEARCH_URL + search).content
    soup = bs(req, 'html.parser')
    a_class = 'linkVideoThumb js-linkVideoThumb img'

    video_list = []
    for item in soup.find_all('a', class_=a_class):
        video_list.append(
            {
                'title': item.find('img')['alt'],
                'video-url': BASE_URL + item['href'],
                'thumb-url': item.find('img')['src']
            }
        )

    num = 0
    disp_videos = []
    for item in video_list:
        print(str(num) + ' - ' + item.get('title'))
        disp_videos.append(item)
        num += 1
        if num > count:
            break

    play(disp_videos)


def play(videos):
    while True:
        selection = click.prompt()
        if not selection:
            print('!')
        elif selection == 'exit':
            break
        else:
            os.command(f'mpv {url}')


if __name__ == '__main__':
    search()
