# sets

items: set = {'apple','bananna',10, True,"apple",True} # we cannot have the duplicate in the set


# they are unorder
# they are non changeable
# we cannot change the set
# we add to the set and remove for the set
# we cannot modify the set

print(items)

# items[0] = 10
name = set([1,2,3,5,6,"apple","ball",'cat'])
print(len(name))


items.update({'carrot', 15})
print(items)



items.pop()

items2: set = {'Carrot', 15,'apple','bananna'}

new_set = items.union(items2)
print(new_set)

new_set = items | items2
print(new_set)

print(new_set)

items.intersection_update(items2) # which give  the duplicates of the items2

new_set = items.symmetric_difference(items2)

print(new_set)