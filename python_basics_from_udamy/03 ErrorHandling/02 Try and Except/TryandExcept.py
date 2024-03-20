print("This is normal error! ")
user_input = input("ENter a number: ")

try:
    number = float(user_input)
    print(number)
except:
    print('Somthing Went wrong.... ')


print('-----------------------------------------------')
print("This is Exception error! ")
# we can also costume our error according to the problem statement

user_input = input("Enter the number Second time: ")

try:
    num = float(user_input)
    print(num)
except Exception as e:
    print(e)

print('----------------------------')
print("This is Value error")

user_input = input("Enter a number: ")

try:
    number = float(user_input)
    print(number)
except ValueError:
    print('Please Enter a valid number! ')

print('------------------------------')

print("This is Zero division error")
user_input = input("Enter a number: ")

try:
    number = float(user_input)
    result = number / 0
    print(result)
except ZeroDivisionError:
    print('Please do not divide by 0 ! ')
except Exception as e:
    print("Something went wrong! ", e)

print('____________________________')
print("you have entered into the function:! ")

def do_math():
    user_input_one = input("Enter a number: ")
    print(user_input_one)

    try:
        number = float(user_input_one)
        print(number)
    except ValueError:
        print("Please enter the valid number! ")
        do_math()
    except ZeroDivisionError:
        print("You have getting the Zero division Error")
    except Exception as e:
        print(e)
        do_math()
do_math()