class car:
    def __init__(self,brand: str, price: int, location: str):
        self.brand = brand
        self.price = price
        self.location = location

    def buy(self):
        print(self.price, "price of the car! ")
        print(self.brand,  "Brand of a car!")

    def no_buy(self):
        print(self.price, 'Price is Too high')
        print(self.location, "very far for the service")

    def describe(self):
        print(f'Car: {self.brand} ({self.price})')

Toyota_car = car('Toyota',1500000, 'Hyderabad')
Toyota_car.buy()
Toyota_car.describe()

