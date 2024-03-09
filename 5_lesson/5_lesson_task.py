# Завдання 1: Робота з функціями
import calculator

def enter_data():
    a = float(input('Type the first number: '))
    b = float(input('Type the second number: '))
    operation = input('Choose the operation (type "+", "-", "*" or "/"): ')
    return a, b, operation

def do_operation(a, b, operation):
    if operation == '+':
        print(calculator.add(a, b))
    elif operation == '-':
        print(calculator.subtract(a, b))
    elif operation == '*':
        print(calculator.multiply(a, b))
    elif operation == '/':
        print(calculator.divide(a, b))
    else:
        print('Wrong operation')

a, b, operation = enter_data()
do_operation(a, b, operation)

# Завдання 2: Створення та імпорт власних модулів

