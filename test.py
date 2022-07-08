import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import pandas as pd
from IPython.display import display

'''Берем ссылку из сайта, откуда нужно спарсить данные'''
URL = 'https://www.akchabar.kg/ru/exchange-rates/'

'''Эта функция вытаскивает данные с таблицы, c помощью пакета Beautifulsoup (анализа документов HTML и XML). rows ищет все данные, которые лежат под тэгом tr. Открываем пустой лист all_rates, куда appendим найденные текстовые данные, которые лежат под определенным индексом [n].'''

page = requests.get(url=URL)
soup = BeautifulSoup(page.text, 'html.parser')
table = soup.find('table', attrs={'id': 'rates_table'})

headers = ['Банк', 'Покупка USD', 'Продажа USD',
           'Покупка EURO', 'Продажа EURO',
           'Покупка RUB', 'Продажа RUB',
           'Покупка KZT', 'Продажа KZT']
data = []

for j in table.find_all('tr')[2:]:
    rows = j.find_all('td')
    row = [i.text for i in rows]
    data.append(row)

#data.remove(data[0])

today = datetime.now().strftime('%d_%m_%Y')
with open(f'pars_data_{today}.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(headers)
    write.writerows(data)

pd_data = pd.read_csv(f'pars_data_{today}.csv')
display(pd_data.to_string())


rows = []
# Считываем данные с файла csv
with open(f'pars_data_{today}.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        rows.append(row)
