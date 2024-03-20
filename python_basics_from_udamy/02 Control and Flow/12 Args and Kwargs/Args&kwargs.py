# Arguments and keywordArguments

print('1','2','3')

def greet_people(age ,*people:str):
    print(people)
    for name in people:
        print(f"hello{name}!")


greet_people(10,"Luigi","Toad")


print("--------------------------")

# Kwargs

def do_somthing(*args, **kwargs):
    print(args)
    print(kwargs)

    print(kwargs['name'])

do_somthing('hello',name = 'Mario', age = 10)






