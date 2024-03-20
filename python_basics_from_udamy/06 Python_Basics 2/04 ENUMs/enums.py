from enum import Enum

class State(Enum):
    OFF = 0
    ON = 1

state = State.ON


if state == State.ON:
    print('The lamp is turned on! ')
    print(State.ON.value)
elif state != State.OFF:
    print('The lamp is turned Off!')

print('-------------------------------------------------')

class Color(Enum):
    RED = 'red'
    BLUE = 'Blue'
    GREEN = 'Green'

c = Color.RED


def check_color(color: Color):
    if color == Color.RED:
        print(color)
        print(color.value)
        print(color.name)
    elif color == Color.BLUE:
        print(color)
    elif color == Color.GREEN:
        print(color)

check_color(Color.BLUE)