from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def f(x):
    total = x
    total -= x // c
    total -= x // d
    total += x // lcm_cd
    return total


a, b, c, d = map(int, input().split())

lcm_cd = lcm(c, d)
print(f(b) - f(a - 1))