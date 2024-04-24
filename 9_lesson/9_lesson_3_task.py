'''
Завдання 3: Принцип підстановки Лісков (Liskov Substitution Principle - LSP)
Створіть ієрархію класів для геометричних фігур, де кожен підклас (наприклад, "Квадрат" і "Круг")
може замінити базовий клас "Фігура" без порушення функціональності. Переконайтеся, що ці підкласи
можуть використовуватися замість базового класу у всіх контекстах без проблем.
'''
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