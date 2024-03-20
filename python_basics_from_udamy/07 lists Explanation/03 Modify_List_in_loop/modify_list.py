people: list[str] = ['Mario','Luigi','peach','Toad']
people2: list[str] = []

for person in people:
    print(person, '->', people)

    if person == 'Luigi':
        pass

    else:
        people2.append(person)

    if person == "Peach":
        print("Hi from Peach!")

print(people2)