string_variable = 'None'
integer_variable = 90
float_variable = 1.5
bool_variable = True
list_variable = ['red', 'green', 'blue']
dict_variable = {'red': 255, 'green': 90, 'blue': 10}
tuple_variable = (1, 2, 3, 4)
none_variable = None

print(string_variable == none_variable)
print(integer_variable > float_variable)
print(len(string_variable) == len(tuple_variable) and bool_variable)
print(dict_variable['red'] == integer_variable or dict_variable['green'] == integer_variable or dict_variable['blue'] == integer_variable)
print(list_variable == dict_variable.keys())

# Робота з рядками
num_str = 125
num_str = str(num_str)
print(type(num_str))

message = 'Hi, my name is Python!'
message = message.replace('y', '0')
message = message.replace('i', '1')
print(message)

split_test = 'This is a split test'
split_test = split_test.split()
string_join = ' '.join(split_test)
print(split_test)
print(string_join)
print(len(string_join))

# Робота зі списками
list_append = [1, 2, 3]
list_append.append(4)
list_append.append(5)
print(list_append)

list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print(list_extend)

print(list_extend.index(6))

print(len(list_append))

# Робота зі словниками
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test['car'])
print(dict_test['where'])

print(dict_test.keys())
print(dict_test.values())

print(dict_test.items())