'''Завдання 2: Параметри запиту
Розширте попереднє завдання, додаючи можливість вказати параметри запиту. Виконайте GET-запит до веб-ресурсу,
передаючи параметри запиту, такі як параметри запиту у URL або параметри через словник.'''

import requests

url_1 = 'https://jsonplaceholder.typicode.com/comments'

body_1 = {
    'postId': 1,
    'id': 2
}

url_2 = 'https://jsonplaceholder.typicode.com/posts/1/comments?id=3'

responce_get = requests.get(url=url_1, params=body_1)
print(responce_get.text)

responce_get = requests.get(url=url_2)
print(responce_get.text)
