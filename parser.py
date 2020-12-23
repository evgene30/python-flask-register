import requests
from bs4 import BeautifulSoup

def parser(URL):

    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'}

    r = requests.get(URL, headers=HEADERS)
    html = BeautifulSoup(r.content, 'html.parser')

    items = html.findAll('div', class_='news-tidings__item news-tidings__item_1of3 news-tidings__item_condensed')

    title = []
    for i in items:
        title.append(i.find('span', class_='news-helpers_hide_mobile-small').get_text(strip=True))
        strong = '\n'.join(title)
        print(strong)
        with open('/Users/flame/Downloads/dataset_3363_3.txt', 'w') as file:
            file.write(str(strong))
        file.close()
    return strong


parser(URL='https://people.onliner.by/')

    items = html.findAll('table', class_='uk-table uk-table-hover uk-table-striped uk-table-divider')  # найти многие элементы в которых содержится текст
    print(items)
    title = []
    for i in items:
        title.append(i.find('p', 'href').get_text(strip=True))  # извлечь текст из элемента
        strong = '\n'.join(title)
        print(strong)

    return strong


parser(URL='http://kontakt.minsk.edu.by/ru/main.aspx?guid=101421')

