import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import pandas as pd
from IPython.display import display


today = datetime.now().strftime('%d_%m_%Y')


def get_table():
    url = 'https://www.akchabar.kg/ru/exchange-rates/'
    pages = requests.get(url)
    soup = BeautifulSoup(pages.text, 'lxml')
    table1 = soup.find('table', id='rates_table')
    return table1


def get_headers():
    headers = []
    table1 = get_table()
    heading = table1.find_all('span', class_='dib')
    heading = [item.text for item in heading]
    for i in heading:
        headers.append(i)
        headers.append(i)
    headers.insert(0, ' ')
    return headers


def pars_data():
    """ Берем ссылку из сайта, откуда нужно спарсить данные"""
    data = []
    table1 = get_table()
    for j in table1.find_all('tr')[1:]:
        rows = j.find_all('td')
        row = [i.text for i in rows]
        data.append(row)
    return data


def write_to_csv(t_headers, my_data):

    with open(f'pars_data_{today}.csv', 'w') as file:
        write = csv.writer(file)
        write.writerow(t_headers)
        write.writerows(my_data)


def show_table():
    pd_data = pd.read_csv(f'pars_data_{today}.csv')
    display(pd_data.to_string().replace('.1', ' '))


def main():
    parsed_data = pars_data()
    write_to_csv(get_headers(), parsed_data)
    show_table()


if __name__ == '__main__':
    main()
