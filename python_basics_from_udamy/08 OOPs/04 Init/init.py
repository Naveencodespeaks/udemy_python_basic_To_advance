class Car:
    def __init__(self, model: str, color: str):
        self.model = model
        self.c = color
        print(f'{self.model}({self.c})')

    def drive(self):
        print(f'{self.model} is now driving')

if __name__ =="__main__":
    car: Car = Car('BMW', 'BLUE')
    car2: Car = Car('Ferrari', 'Red')


    car.drive()
    car2.drive()


