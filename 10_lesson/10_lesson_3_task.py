'''Завдання 3: POST-запит
Створіть Python-сценарій для виконання POST-запиту до веб-ресурсу. Відправте дані на сервер, наприклад,
форму з ім'ям користувача і паролем.'''

import requests

url = 'https://jsonplaceholder.typicode.com/posts'

body = {
    'userName': 'Dario Srna',
    'password': 'qwerty1234'
}

responce_post = requests.post(url=url, data=body)

print(responce_post.status_code)
print(responce_post.text)
