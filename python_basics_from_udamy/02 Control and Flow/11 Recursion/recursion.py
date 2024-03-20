# behave like the loop
def do_something(n:int):
    print(n)
    if n == 1:
        print("Done with function! ")
        return
    do_something(n - 1)

do_something(3)
# next line
