# Завдання 1: Наслідування

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Це {self.make} {self.model} {self.year} року виробництва.")
    

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type
    
    def start_engine(self):
        print(f'Your engine is started')

    def display_info(self):
        super().display_info()
        print(f"Тип палива: {self.fuel_type}.")



class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_value):
        super().__init__(make, model, year)
        self.engine_value = engine_value

    def start_engine(self):
        print(f'Wrroooom!')

    def display_info(self):
        print(f"Це мотоцикл {self.make} {self.model} {self.year} року виробництва із об'ємом двигуна {self.engine_value} куб.см.")


class Bicycle(Vehicle):
    def __init__(self, make, model, year, speeds_number):
        super().__init__(make, model, year)
        self.speeds_number = speeds_number

    def display_info(self):
        super().display_info()
        print(f'Кількість швидкостей велосипеда: {self.speeds_number}.')


car1 = Car('volkswagen', 'Polo', 2002, 'diesel')
car1.start_engine()
bike1 = Motorcycle('Honda', 'Any', 2023, 125)
bike1.start_engine()
bike2 = Bicycle('KhVZ', 'Ukraina', 1989, 1)

for vehicle in (car1, bike1, bike2):
    print (vehicle.__dict__)
    

# Завдання 2: Поліморфізм

for vehicle in (car1, bike1, bike2):
    print('---------------------')
    vehicle.display_info()
