for i in range(10):
    print(i)
    if i == 5:
        break
print("Done!")

print('-----------------------')

i = 0

while i < 3:
    print(i)
    if i == 1:
        break
    i += 1
print('-----------------------------')

for i in range(5):
    if i == 3:
        continue
    print(i)

    if i ==4:
        print("Break triggered! ")
        break
    print(i)