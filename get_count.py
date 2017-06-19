import requests
from bs4 import BeautifulSoup


def get_count_from_price(page_num):
    num = 0
    res_pr = []
    for i in range(page_num):
        paginator = 'https://realty.domclick.ru/prodazha-kvartir/?addresses=0c5b2444-70a0-4932-980c-b4dc0d3f02b5&' \
                    'region=0c5b2444-70a0-4932-980c-b4dc0d3f02b5&with_photo=1&offset={}'.format(str(num))
        page = requests.get(paginator).text
        soup = BeautifulSoup(page, features='html.parser')
        num += 30
        prices = soup.find_all(class_='offer-snippet__title')
        for pr in prices:
            sp = pr.find('span')
            res_pr.append(int(sp.text.replace(' ', '')))
    return sum(res_pr) / len(res_pr)


def get_count_from_every_page(page_num):
    num = 0
    res_pr = []
    count_from_page = []
    for i in range(page_num):
        paginator = 'https://realty.domclick.ru/prodazha-kvartir/?addresses=0c5b2444-70a0-4932-980c-b4dc0d3f02b5&' \
                    'region=0c5b2444-70a0-4932-980c-b4dc0d3f02b5&with_photo=1&offset={}'.format(str(num))
        page = requests.get(paginator).text
        soup = BeautifulSoup(page, features='html.parser')
        num += 30
        prices = soup.find_all(class_='offer-snippet__title')
        for pr in prices:
            sp = pr.find('span')
            res_pr.append(int(sp.text.replace(' ', '')))
        count_from_page.append(sum(res_pr) / len(res_pr))
    return count_from_page

print(get_count_from_price(1))
print(get_count_from_every_page(2))
