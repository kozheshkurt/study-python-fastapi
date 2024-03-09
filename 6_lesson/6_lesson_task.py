# Завдання 1: Створення класу і об'єктів

class Animal():
    '''Creates new animal'''
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    
    def make_sound(self):
        if self.species == 'cat':
            print('Meow!')
        elif self.species == 'dog':
            print('Woof!')
        else:
            print('Hello!')
    
animal1 = Animal('Tom', 'cat', '3')
animal2 = Animal('Jerry', 'mouse', '2')

animal1.make_sound()
animal2.make_sound()
        
# Завдання 2: Робота з об'єктами

class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.check_geometry()
        print(self.__dict__)

    def check_geometry(self):
        for attr in self.__dict__:
            if isinstance(self.__dict__[attr], str):
                print (f'Incorrect {attr}')
                setattr(self, attr, 1)
            if getattr(self, attr, False) < 0:
                print ("Size can't be negative")
                setattr(self, attr, 0)

    def calculate_area(self):
        area = self.width * self.height
        print (f'Area of the rectangle {self.width}x{self.height} is {area}')



rect1 = Rectangle(5, 6)
rect1.calculate_area()

rect2 = Rectangle(-5, 6)
rect2.calculate_area()

rect3 = Rectangle(5, 'xyz')
rect3.calculate_area()

rect4 = Rectangle(10, 1.5)
rect4.calculate_area()