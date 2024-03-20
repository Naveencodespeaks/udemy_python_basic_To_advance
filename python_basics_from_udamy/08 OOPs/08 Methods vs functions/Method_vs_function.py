class Fruit:
    def __init__(self,name: str, calories: float):
        self.name = name
        self.calories = calories

    def explode(self,weight:int, rate:int):
        self.weight = weight
        self.rate = rate
        print(self.name,'the weight is : ',self.weight,'The rate of the fruit :',self.rate,'exploded!')

    def eat(self):
        print(self.name, 'Has been eaten!',': Has the calories of : ',self.calories)


def hello():
    print('Hello')


Fruit('Banana',10).eat()

Fruit('Apple',20).explode(20,100)
Fruit('mango',50).explode(30,40)
hello()
