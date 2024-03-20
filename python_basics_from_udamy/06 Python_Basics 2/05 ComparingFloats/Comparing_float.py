a = 0.3
b = 0.1 + 0.2

print(a)
print(b)
print(a == b)


def compare_float(a:float, b:float, tol:float) -> bool:
    absolute = abs(a - b )
    print(f'{a} - {b} = {a -b }')
    return absolute < tol

first = 0.8
second = 0.1 + 0.71

compare_float(first,second,tol = 1e-10) # 0.00000000117