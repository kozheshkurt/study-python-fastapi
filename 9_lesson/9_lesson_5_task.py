'''
Завдання 5: Принцип залежностей (Dependency Inversion Principle - DIP)
Використовуючи принцип DIP, переробіть код залежностей у вашому проекті так, щоб він
використовував абстракції та інтерфейси замість конкретних реалізацій. Переконайтеся,
що класи залежностей не знають про конкретну реалізацію інших класів.
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
            print('You are in the queue, please wait.')
        else:
            print('Scanning goes. Take back your document.')

    def drucken(self, user_number):
        if user_number > self.users_number:
            print('You are in the queue, please wait.')
        else:
            print('Printing goes. Take back your document.')



class Printer(Druckung):

    def __init__(self, name):
        self.name = name

    def drucken(self):
        print(f'Printing on the {self.name} goes.')


class Scanner(Scannung):

    def __init__(self, name):
        self.name = name

    def scanen(self):
        print(f'Scanning on the {self.name} goes.')


class PowerManage:

    def __init__(self, device):
        self.device = device
    
    def power_on(self):
        print(f'Your {self.device.name} is ON.')

    def power_off(self):
        print(f'Your {self.device.name} is OFF.')


network_printer = NetworkPrinter('Samsung', 3)
network_printer_power = PowerManage(network_printer)
network_printer_power.power_on()