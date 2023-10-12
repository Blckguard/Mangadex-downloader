from time import sleep
from requests import get
from shutil import *



def get_id():
    ''' takes a url and returns an id for the given manga
        returns: string '''

    manga_url = input('manga url: ')
    return manga_url.split('/')[4]

def get_chapters():
    ''' creates a list of chapters for the given manga
        returns: list'''

    manga_id = get_id()
    chapters_list = []
    total = 1
    offset = 0
    successful = False

    # config
    translated_language = 'en'
    order = ''
    chapter = ''

    headers = {
        'User-Agent':  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        'From': ''  # This is another valid field
    }

    while not successful:
        if len(chapters_list) == total:
            successful = True
        else:
            request_list = get(f'''https://api.mangadex.org/chapter?manga={manga_id}&offset={offset}{order}{chapter}&limit=50&translatedLanguage[]={translated_language}''', headers = headers).json()

            if request_list['result'] == 'error':
                print(request_list)
                break
            offset += 50
            total = request_list['total']
            chapters_list += request_list['data']
            sleep(0.2)
    return chapters_list


chapters_list = get_chapters()

res = get(f"https://mangadex.org/chapter/{chapters_list[2]['id']}/2", stream = True)

if res.status_code == 200:
    with open('page.png','wb') as f:
        copyfileobj(res.raw, f)
    print('Image sucessfully Downloaded: ')
else:
    print('Image Couldn\'t be retrieved')