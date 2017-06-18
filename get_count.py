import requests
from bs4 import BeautifulSoup


def get_count_from_price(page_num):

    if page_num > 0:
        get_info_from_main_page = requests.get(
            'https://realty.domclick.ru/prodazha-kvartir/?with_photo=1&addresses=0c5b2444-70a0-4932-980c-b4dc0d3f02b5&region=0c5b2444-70a0-4932-980c-b4dc0d3f02b5').text

        soup = BeautifulSoup(get_info_from_main_page, features='html.parser')

        prices = soup.find_all(class_='offer-snippet__title')

        res_pr = []

        for i in range(page_num):
            page_num = 30
            paginator = 'https://realty.domclick.ru/prodazha-kvartir/?addresses=0c5b2444-70a0-4932-980c-b4dc0d3f02b5&offset={}&region=0c5b2444-70a0-4932-980c-b4dc0d3f02b5&with_photo=1'.format(
                str(page_num))
            requests.get(paginator)
            page_num += 30
            for pr in prices:
                sp = pr.find('span')
                # удаляем пробелы в цене
                res_pr.append(int(sp.text.replace(' ', '')))
    else:
        raise Exception('Number less 0')
    return sum(res_pr)/ len(res_pr)

print(get_count_from_price(1))