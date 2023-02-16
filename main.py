from requests import *
from time import *

url = 'https://mangadex.org/title/a77742b1-befd-49a4-bff5-1ad4e6b0ef7b/chainsaw-man'
id = url.split('/')[4]

chapter_list = get(f'https://api.mangadex.org/chapter?manga={id}&limit=10&translatedLanguage[]=en').json()

if chapter_list['result'] == 'error':
    print(chapter_list)
else:
    for i in chapter_list['data']:
        print(i['attributes']['chapter'], i['attributes']['title'], i['attributes']['pages'])
        sleep(0.3)