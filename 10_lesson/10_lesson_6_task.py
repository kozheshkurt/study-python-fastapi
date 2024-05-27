'''Завдання 6: Збереження вмісту в файл
Розширте ваш код, щоб зберегти отриманий вміст веб-сторінки у файл. Використайте функціонал Python для роботи
з файлами для збереження вмісту.'''

import requests
from bs4 import BeautifulSoup

def show_h3_titles(url):
    responce_get = requests.get(url=url)

    if responce_get.status_code == 200:
        soup = BeautifulSoup(responce_get.text, features="html.parser")

        titles = soup.find_all('h3')
        page = ''

        for title in titles:
            text = title.text.strip()
            print(text)
            page = page + text + '\n'
        return page

    elif responce_get.status_code == 400:
        print('Please change your request to the correct one')

    elif responce_get.status_code == 404:
        print('URL is not found')
    
    else:
        print('Undefined error')



url1 = 'https://football.ua/germany/531730-chomu-bavarija-khoche-priznachiti-golovnim-trenerom-kompani.html'

text = show_h3_titles(url1)

fh = open('h3 tags.txt', 'w')
fh.write(str(text))
fh.close()