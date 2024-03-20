user_input: str = input("You: ")

if user_input == '0':
    raise Exception('please never use 0!')


print('-------------------')
is_connected: bool = False

def connect_to_internet():
    if not is_connected:
        raise ConnectionError('No internet! ')
    else:
        print('Connected to the internet! ')


try:
    connect_to_internet()
except ConnectionError:
    print("There is no connection")
except Exception as e:
    print(e)
