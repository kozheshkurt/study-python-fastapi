'''Завдання 5: Обробка помилок
Додайте обробку помилок до вашого коду. Обробляйте можливі винятки, такі як requests.exceptions.RequestException,
та виводьте відповідні повідомлення про помилку.'''

import requests
from bs4 import BeautifulSoup

def show_h3_titles(url):
    responce_get = requests.get(url=url)

    if responce_get.status_code == 200:
        soup = BeautifulSoup(responce_get.text, features="html.parser")

        titles = soup.find_all('h3')

        for title in titles:
            text = title.text
            print(text)

    elif responce_get.status_code == 400:
        print('Please change your request to the correct one')

    elif responce_get.status_code == 404:
        print('URL is not found')
    
    else:
        print('Undefined error')



url1 = 'https://football.ua/germany/531730-chomu-bavarija-khoche-priznachiti-golovnim-trenerom-kompani.html'
url2 = 'https://football.ua/germany/531730-chomu-bavarija-hoche-priznachiti-golovnim-trenerom-kompani.html'


show_h3_titles(url1)
show_h3_titles(url2)
