class Connection:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            print('Connecting...')
            cls.__instance = super().__new__(cls)
            return cls.__instance
        else:
            print("Waring: There\'s already a connection.")
            return cls.__instance

    def __init__(self):
        print('Connected to internet! ')



connection = Connection()
connection2 = Connection()
print(connection == connection2)

