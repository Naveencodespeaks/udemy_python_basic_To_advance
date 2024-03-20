class Fruit:
    def __init__(self, name: str, calories: float):
        self.name = name
        self.calories = calories

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


if __name__ == "__main__":
    apple1 = Fruit('Apple', 10)
    apple2 = Fruit('Apple', 10)
    orange = Fruit('orange','20')

    print(apple1 == apple2)
    print(apple1 == orange)
