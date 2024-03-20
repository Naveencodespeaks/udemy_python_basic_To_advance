def standard_arg(arg):
    print(arg)

# every thing before the slash positional only.
def pos_only_arg(arg1, arg2, /):
    print(arg1, arg2)

def kwd_only_arg(*people, arg1, arg2):
    print(people, arg1, arg2)

def combination_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard,kwd_only)


standard_arg("Harekrishna")

if __name__ =='__main__':
    # which only takes the positional arguments.
    pos_only_arg(1,2)
    kwd_only_arg('bob','joe','Jhon', arg1 = 1, arg2 = 2)
    combination_example(1,2,3,4,5,5,kwd_only=20)
