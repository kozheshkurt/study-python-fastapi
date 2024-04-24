'''
Завдання 2: Принцип відкритості/закритості (Open/Closed Principle - OCP)
Створіть інтерфейс "Фігура" (Shape) та два класи, які реалізують цей інтерфейс,
наприклад, "Коло" (Circle) та "Прямокутник" (Rectangle). Потім додайте новий клас,
який розраховує площу будь-якої фігури, не модифікуючи існуючі класи. Використовуйте
принцип OCP для розширення функціональності.
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
    
class AnyFigure(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_area(self):
        area = self.a*self.b
        return area
