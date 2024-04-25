'''Завдання 1: Виконання GET-запиту
Створіть Python-сценарій, який використовує бібліотеку requests для виконання GET-запиту до веб-ресурсу
та виведення вмісту веб-сторінки на екран. Використовуйте функцію requests.get() для виконання запиту.'''

import requests

url = 'https://jsonplaceholder.typicode.com'

responce_get = requests.get(url=url)
print(responce_get.text)
