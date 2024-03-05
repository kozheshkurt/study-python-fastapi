### Списки:
# Робота із списками:
lst = [1, 2, 3, 5, 7, 11, 13, 17]
lst.append(10)
lst.append(20)
lst.remove(10)
print(lst)

# Знаходження суми:
lst = [1, 2, 3, 5, 7]
total = 0

for num in lst:
    total += num

print(total)

# Подвійні значення:
lst = [1, 2, 3, 5, 7]

for i in range(len(lst)):
    lst[i] = lst[i]*2

print(lst)

### Кортежі:
# Робота із кортежами:
tup = ("яблуко", "банан", "апельсин")

for fruit in tup:
    print(fruit)

# Об'єднання кортежів:
num_tup_1 = (1, 2, 3, 4)
num_tup_2 = (10, 20, 30)
united_num_tup = num_tup_1 + num_tup_2
print(united_num_tup)

### Словники
# Робота із словниками:
sportsman = {
    'Name': 'Dario',
    'Last name': 'Srna',
    'Age': 41,
    'Sport': 'Football',
    'Team': 'Shakhtar'
}

for key, value in sportsman.items():
    print(f'{key}: {value}.')

# Оновлення словника:
books = {
    '1984': 1949,
    'Brave New World': 1932
}

books.update({'Fahrenheit 451': 1953})

print(books)

# Пошук значення:
capitals = {
    'Ukraine': 'Kyiv',
    'Poland': 'Warsaw',
    'Germany': 'Berlin',
    'Austria': 'Wien',
    'France': 'Paris',
    'Netherlands': 'Amsterdam'
}

capital = capitals.get('Spain')

if capital:
    print(capital)

capital = capitals.get('Germany')

if capital:
    print(capital)

