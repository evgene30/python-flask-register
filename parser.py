import requests
from bs4 import BeautifulSoup


def parser(URL):

    global strong
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
