# Dictionary

people={}

print(people)

user = {'user1': "Mario123",
        'user2': 'Luigi456',
        'user3': 'Shy Guy'}

print(user)
print(len(user))

user2=user['user1']
print(user2)

# user1 = user['u']
# print(user1)

x = user.get('X')
print(x)  # which return the None

x = user.keys()
print(x)

user['user1'] = 'Toad34'
print(user)

x = user.items()
print(x)

x = list(user.values())
print(x)

x = list(user.keys())
print(x)

users = {'user1': "naveen"}
y = users.update({'hello': 124})  # update will only returns None
print(users)
print("_______________")

users.pop('user1')
print(users)

print('___________')
users.clear()
print(users)
print("------------------")

user = {'user1': "Mario123",
        'user2': 'Luigi456',
        'user3': 'Shy Guy',
        'items': {'apple': 19, 'bananna': 20}}

print(user['items']['apple'])

print(users.setdefault('user1', 'There is no key!'))
print(users)
