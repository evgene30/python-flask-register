from bs4 import BeautifulSoup


def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    result = []

    trs = soup.find_all('tr')[1:]
    for tr in trs:
        tds = tr.find_all('td')

        name = tds[0].getText()
        status = tds[2].getText()
        result.append({
            'id': name,
            'status': status,
        })

    return result


def main():
    with open('index.html') as f:
        html = f.read()

    result = parse(html)
    print(result)


if __name__ == '__main__':
    main()