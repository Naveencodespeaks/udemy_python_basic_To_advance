people: tuple = ('Mario','Luigi', 'peach','Shy Guy')

people1: tuple = 'Mario',
print(people)
print(people1)

people[0] = 'Wario' # tupels are not changeable

print(len(people))

people_list: list[str] = list(people)
people_tuple: tuple= tuple(people_list)
print(people_list)


print(people[2:4])
print(people[:2])
print('Mario' in people)

print(people.count('Mario'))

print(people.index('Mario'))

a,b,c,d = people
print(a)
print(b)
print(d)

a, *b = people
print(a)




