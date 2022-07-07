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

# Создаем цыкл для заполнения mydata
for j in table1.find_all('tr')[1:]:
    row_data = j.find_all('td')
    row = [i.text for i in row_data]
    length = len(mydata)
    mydata.loc[length] = row

# Удаляю первую запись с индексом 0 row
mydata.drop(labels=[0], axis=0, inplace=True)


# Импортирую в csv
last_dt = datetime.now().strftime('%d_%m_%Y')
mydata.to_csv(f'my_data_{last_dt}.csv', index=False)

# Считываем данные с файла csv
mydata2 = pd.read_csv(f'my_data_{last_dt}.csv')

display(mydata2.to_string())
