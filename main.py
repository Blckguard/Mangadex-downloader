from requests import *
from time import *
from PyQt5.QtWidgets import *

url = input('manga url: ')

def get_id(url):
    # takes a url and returns an id for the given manga
    # returns: string

    return url.split('/')[4]

def get_chapters():
    # creates a list of chapters for the given manga
    # returns: list

    id = get_id(url)
    chapters = []
    total = 1
    offset = 0
    successful = False

    while not successful:
        if len(chapters) == total:
            successful = True
        else:
            request_list = get(f'https://api.mangadex.org/chapter?manga={id}&limit=50&translatedLanguage[]=en&offset={offset}').json()
            offset += 50
            total = request_list['total']
            chapters = chapters + request_list['data']
            sleep(0.2)
    return chapters

chapters = get_chapters()
print(len(chapters))

