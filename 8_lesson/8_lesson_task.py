#Завдання 1: Інкапсуляція

class User():
    
    def __init__(self, name, email, password):
        self.__name = name
        self.__email = email
        self.__password = password

    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email
    
    def get_password(self):
        return self.__password

     
    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password


user = User('Name Familienname', 'abcd@gmail.com', 'qwertz1234')
user.set_name('Albert Einstein')
user.set_email('einstein@gmail.com')
user.set_password('**e=mc^2**')

print(f'Hello, {user.get_name()} ({user.get_email()}), your password is: {user.get_password()}')


#Завдання 2: Абстракція

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = 3.14 * self.radius * self.radius
        return area
    

class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        area = self.width * self.height
        return area 
    

class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        half_perimeter = (self.a + self.b + self.c) / 2
        area = (half_perimeter * (half_perimeter - self.a) * (half_perimeter - self.b) * (half_perimeter - self.c))**0.5
        return area
    

circle = Circle(2)
rectangle = Rectangle(3, 4)
triangle = Triangle(4, 5, 3)

print(f'Area of circle = {circle.calculate_area()}')
print(f'Area of rectangle = {rectangle.calculate_area()}')
print(f'Area of triangle = {triangle.calculate_area()}')