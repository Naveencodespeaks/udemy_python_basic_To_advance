user_input: str = input('you: ')

try:
    number = float(user_input)
    print(number)
except Exception as e:
    print('Exception: ', e)
else:
    print("Successfully executed the code! ")
finally:
    print("This will always run! ")


# else block run the code when the code run with no exceptions