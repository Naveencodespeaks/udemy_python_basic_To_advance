# Type conversion

name = "Mario"
number = 10
# TypeError: can only concatenate str (not "int") to str
# print(name + number)

print(name + str(number))
print('---------------------------')
result = name + str(number)
print(result)

number_hundred = '100'
number = 10

result = str(number) + (number_hundred)
print('-----------------------')
print(result)
print('-----------------')
result = number + int(number_hundred)
print(result)