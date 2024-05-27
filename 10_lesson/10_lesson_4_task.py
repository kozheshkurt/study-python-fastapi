'''Завдання 4: Обробка відповіді
Після виконання запиту, розпарсьте вміст HTTP-відповіді та виведіть потрібну інформацію. Наприклад,
виведіть заголовки відповіді або вміст сторінки.'''

import requests
from bs4 import BeautifulSoup

url = 'https://football.ua/germany/531730-chomu-bavarija-khoche-priznachiti-golovnim-trenerom-kompani.html'

responce_get = requests.get(url=url)

soup = BeautifulSoup(responce_get.text, features="html.parser")

titles = soup.find_all('h3')

for title in titles:
    text = title.text
    print(text)

