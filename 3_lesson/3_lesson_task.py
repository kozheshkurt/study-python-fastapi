# Умовні конструкції

# **Перевірка паролю:**

correct_password = 'password123'
inputed_password = 'password123'

if inputed_password == correct_password:
    print("Ви увійшли в систему")
else:
    print("Неправильний пароль")

# **Визначення днів тижня:**

days_of_week = {
    1: 'понеділок',
    2: 'вівторок',
    3: 'середа',
    4: 'четвер',
    5: "п'ятниця",
    6: 'субота',
    7: 'неділя'
}

number_of_day = 3

if number_of_day < 1 or number_of_day > 7:
    print('Номер дня тижня некоректний')
else:
    print(f'День номер {number_of_day} - це {days_of_week[number_of_day]}')

# Цикли:

# **Таблиця множення:**

number_for_table = 6
size_of_table = 10
i = 1

while i <= 10:
    print(f"{number_for_table} * {i} = {number_for_table * i}")
    i += 1

# **Сума чисел:**
lst = [2, 4, 7, 1, 10]
total = 0

for n in lst:
    total = total + n

print("Сума дорівює ", total)

# **Факторіал числа:**
number_for_factorial = 5
factorial = 1

if number_for_factorial < 0:
    factorial = None
elif number_for_factorial == 0:
    factorial = 1
else:
    i = 1
    while i <= number_for_factorial:
        factorial = factorial * i
        i += 1

if factorial:
    print('Факторіал дорівнює ', factorial)
else:
    print('Некоректне число')

# **Парні числа:**
i = 1
even_numbers = []

while i <= 50:
    if i % 2 == 0:
        even_numbers.append(i)
    i += 1

print(even_numbers)

# **Пошук простих чисел:**

start_point = 5
end_point = 15

simples = []
i = start_point

while i <= end_point:
    i_is_simple = True
    for j in range(i):
        if i % (j+1) == 0 and j+1 != 1 and j+1 != i:
            i_is_simple = False
    if i_is_simple:
        simples.append(i)
    i += 1

print(f"В діапазоні від {start_point} до {end_point} прості числа: {simples}")