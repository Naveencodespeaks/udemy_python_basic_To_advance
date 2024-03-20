file = open('sample.txt')
text = file.read()
file.close()

print(text)
print('------------------------------')
print('-----------------with keyword-----------------')
with open('sample.txt') as file:
    text = file.read()
    print(text)