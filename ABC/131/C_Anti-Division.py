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



# ---------------------------
from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def calc(x):
    return B // x - (A - 1) // x


A, B, C, D = map(int, input().split())

total = B - A + 1
c = calc(C)
d = calc(D)
cd = calc(lcm(C, D))
print(total - c - d + cd)
