import requests
from bs4 import BeautifulSoup


def parser(URL):
    global strong

    HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'}

    r = requests.get(URL, headers=HEADERS)
    html = BeautifulSoup(r.content, 'html.parser')
    items = html.findAll('table', class_='uk-table uk-table-hover uk-table-striped uk-table-divider')  # найти многие элементы в которых содержится текст
    print(items)
    title = []
    for i in items:
        title.append(i.find('p', 'href').get_text(strip=True))  # извлечь текст из элемента
        strong = '\n'.join(title)
        print(strong)
        # with open('/Users/flame/Downloads/Новости.txt', 'w') as file:
        #    file.write(str(strong))
        # file.close()
    return strong


parser(URL='http://kontakt.minsk.edu.by/ru/main.aspx?guid=101421')
