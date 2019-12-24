from bs4 import BeautifulSoup as bs
import requests



SEARCH_URL = 'https://www.pornhub.com/video/search?search='
BASE_URL = 'https://www.pornhub.com'


def search(keywords, amount):
    req = requests.get(SEARCH_URL + search).content
    soup = bs(req, 'html.parser')
    a_class = 'linkVideoThumb js-linkVideoThumb img'

    num = 0
    video_list = []
    for item in soup.find_all('a', class_=a_class):
        video_list.append(
            {
                'title': item.find('img')['alt'],
                'video-url': BASE_URL + item['href'],
                'thumb-url': item.find('img')['src'],
                'video_id': num
            }
        )
        num += 1
        if num > amount:
            break

        return video_list


def play(videos, video_id):
    pass
