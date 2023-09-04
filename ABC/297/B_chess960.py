def is_ok1():
    x = S.find('B')
    y = S.rfind('B')
    return x % 2 != y % 2

def is_ok2():
    x = S.find('R')
    y = S.rfind('R')
    z = S.find('K')
    return x < z < y

S = input()
print("Yes" if is_ok1() and is_ok2() else "No")