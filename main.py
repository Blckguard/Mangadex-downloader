from time import sleep
from requests import get



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
    order = ''
    chapter = ''

    while not successful:
        if len(chapters_list) == total:
            successful = True
        else:
            request_list = get(f'''https://api.mangadex.org/chapter?manga={manga_id}&offset={offset}{order}{chapter}&limit=50&translatedLanguage[]=en''').json()

            if request_list['result'] == 'error':
                print(request_list)
                break
            offset += 50
            total = request_list['total']
            chapters_list += request_list['data']
            sleep(0.2)
    return chapters_list


chapters = get_chapters()
print(len(chapters))
