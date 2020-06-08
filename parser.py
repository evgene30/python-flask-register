import requests
from bs4 import BeautifulSoup

#URL = str(input('Введите ссылку: '))
URL = 'https://www.tut.by/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
           'accept': '*/*'}

#HOST = 'http://kontakt.minsk.edu.by/ru/'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div').get_
    print(items)

    name = []
    for item in items:
        name.append({
            'Название': item.find('entry-cnt').get_text(strip=True),
            #'Ссылка': HOST + item.find('a').get('href')
        })
    print(name)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Error')


parse()
