from typing import Protocol

class Printable(Protocol):
    pages: int

    def print(self):
        pass
    def recycle(self):
        pass

class Book:
    pages:int
    def __init__(self,title:str):
        self.title = title

    def print(self):
        print('Printing book: ', self.title)
    def recycle(self):
        print('Recycling Book: ', self.title)


class Magazine:
    pages:int
    def __init__(self,title:str):
        self.title = title

    def print(self):
        print('Printing Magazine: ', self.title)
    def recycle(self):
        print('Recycling Magazine: ', self.title)


def print_item(printable: Printable):
    printable.print()


book: Printable = Book('Python')
print_item(book)

magazine: Printable = Magazine('Deluxe Magazine')
print_item(magazine)