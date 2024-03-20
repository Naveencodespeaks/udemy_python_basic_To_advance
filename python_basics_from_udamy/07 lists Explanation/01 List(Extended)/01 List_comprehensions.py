# list comprehension
sample_list = []

for i in range(10):
    if i % 2 == 0:
        sample_list.append(i)


print(sample_list)

# [result for elements in list ]
sample_list2 = [i for i in range(10) if i % 2 == 0]
print(sample_list2)


print('-----------------------------------')

people: list[str] = ['Mario','Luigi','Peach']

cap_people = [person.upper() for person in people ]
print(cap_people)