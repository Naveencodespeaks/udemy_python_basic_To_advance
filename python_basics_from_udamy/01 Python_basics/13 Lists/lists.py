people: list[str] = ['Mario', 'Luigi', 'Peach', 'Peach', 'Toad']
print(people)

print(len(people))

print(people[0])
print(people[1])
print(people[2])
print(people[3])
print(people[4])
print(people[-1])
print(people[-2])
print(people[-3])
print(people[-4])

print(people[0:4])

print(people[2:4])
print(people[0:18:1])

print('Luigi' in people)

people[0] = 'Shy Guy'
print(people)

people[0:2] = ['Shy Guy', 'Bowser' ]

print(people)

people.insert(2,'!!!!')
print(people)

people.append('shy Guy')

print(people)

people2: list[str] =   ['Sonic', 'Tails']
new_list = people + people2
print(new_list)




people.remove('Shy Guy')
print(people)

people.pop()
print(people)

people.reverse()
people.remove('Luigi')
# remove() will removes the first occurance of the list




