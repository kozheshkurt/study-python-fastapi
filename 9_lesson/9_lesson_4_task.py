'''
Завдання 4: Принцип інтерфейсу користувача (Interface Segregation Principle - ISP)
Розробіть інтерфейс "Мережевий принтер" (NetworkPrinter), який включає методи для друку,
сканування та копіювання. Потім створіть два класи: "Принтер" (Printer) та "Сканер" (Scanner),
які реалізують цей інтерфейс та використовують лише ті методи, які їм потрібні. Переконайтеся,
що жоден з класів не має пустого методу.
'''
from abc import ABC, abstractmethod

class Scannung(ABC):

    @abstractmethod
    def scanen(self):
        pass


class Druckung(ABC):

    @abstractmethod
    def drucken(self):
        pass


class NetworkPrinter(Scannung, Druckung):
    
    def __init__(self, name, users_number):
        self.users_number = users_number
        self.name = name
    
    def scanen(self, user_number):
        if user_number > self.users_number:
            print('You are in the queue, please wait')
        else:
            print('Scanning goes. Take back your document')

    def drucken(self, user_number):
        if user_number > self.users_number:
            print('You are in the queue, please wait')
        else:
            print('Printing goes. Take back your document')



class Printer(Druckung):

    def __init__(self, name):
        self.name = name

    def drucken(self):
        print(f'Printing on the {self.name} goes')


class Scanner(Scannung):

    def __init__(self, name):
        self.name = name

    def scanen(self):
        print(f'Scanning on the {self.name} goes')


scanner = Scanner('Samsung')
scanner.scanen()

networkprinter = NetworkPrinter('Hp', 3)
networkprinter.drucken(4)
networkprinter.drucken(3)