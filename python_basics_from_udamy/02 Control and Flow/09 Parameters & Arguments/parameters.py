def hello():
    print('Hello')


hello()
hello()
hello()
hello()

def greet(name: str, greeting: str = 'Hello', age :int = 0 ):
    print(f'{greeting},{name}!{age} ')


greet(name = 'mario',greeting = 'Ciao',age = 16)