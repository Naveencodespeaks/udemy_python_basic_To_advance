class Animal:
    def __init__(self, name : str):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f'{self.name} is sleeping. ')

class Cat(Animal):
    def __init__(self, name: str, weight: float):
        super().__init__(name)
        self.weight = weight

    def meow(self):
        print(f'Name of the cat: {self.name}:-  says "Meow" ')


class Dog(Animal):
    def __init__(self, name: str, job: float):
        super().__init__(name)
        self.job = job

    def work_at_job(self):
        print(f'Name of the dog: "{self.name}":-  is working  as a {self.job} ')



if __name__ == "__main__":

    cat: Cat = Cat('Apple',100)
    dog: Dog  = Dog('Waffles', 'chef')
    dog.work_at_job()
    dog.sleep()


    cat.meow()
    cat.sleep()

