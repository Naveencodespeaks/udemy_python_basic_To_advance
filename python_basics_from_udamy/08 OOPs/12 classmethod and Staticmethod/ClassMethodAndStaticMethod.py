class Calculator:
    var: int
    def __init__(self,name: str):
        self.name = name

    def descripiton(self):
        print(f"{self.name} is a calculator! ")

    @staticmethod
    def add_numbers(a: float, b: float):
        print(a + b )

    @classmethod
    def create_with_version(cls,name: str, version:int):

        return cls(f'{name}: ({version})')

calc: Calculator = Calculator.create_with_version('Bob',100)
calc.descripiton()

calc: Calculator = Calculator('jeff')
calc.descripiton()
calc.add_numbers(1,2)
Calculator.add_numbers(10,30)