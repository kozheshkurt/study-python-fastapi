'''
Завдання 1: Принцип єдиного обов'язку (Single Responsibility Principle - SRP)
Спроектуйте і реалізуйте клас "Користувач" (User), який відповідає принципу SRP.
В цьому класі повинні бути методи для створення користувача, оновлення даних
користувача та видалення користувача. Переконайтеся, що кожен метод відповідає
за одну конкретну функцію.
'''

class User():
    
    def __init__(self, nickname, mail, password):
        self.nickname = nickname
        self.mail = mail
        self.password = password

    def update_nickname(self, new_nickname):
        self.nickname = new_nickname
    
    def update_mail(self, new_mail):
        self.mail = new_mail

    def update_password(self, new_password):
        self.password = new_password
    
    def delete(self):
        self.nickname = None
        self.mail = None
        self.password = None

user_1 = User('Nick', 'abc@gmail.com', 'qwerty123')
user_1.update_password('QwErTy123')
print(f'Username: {user_1.nickname}, e-mail: {user_1.mail}, password: {user_1.password}')
user_1.delete()
print(f'Username: {user_1.nickname}, e-mail: {user_1.mail}, password: {user_1.password}')