import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from IPython.display import display


url = 'https://www.akchabar.kg/ru/exchange-rates/'
pages = requests.get(url)
soup = BeautifulSoup(pages.text, 'lxml')
table1 = soup.find('table', id='rates_table')

# Шапка нашего датафрейма
headers = ['Банк', 'Покупка USD', 'Продажа USD',
           'Покупка EURO', 'Продажа EURO',
           'Покупка RUB', 'Продажа RUB',
           'Покупка KZT', 'Продажа KZT']

# Создание датафрейма
mydata = pd.DataFrame(columns=headers)

# Создаем цикл для заполнения mydata
t_body = table1.find('tbody')
for j in t_body.find_all('tr'):
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    length = len(mydata)
    mydata.loc[length] = row

# Импортирую в csv
last_dt = datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
mydata.to_csv(f'my_data_{last_dt}.csv', index=False)

# Считываем данные с файла csv
mydata2 = pd.read_csv(f'my_data_{last_dt}.csv')

display(mydata2.to_string())

