from functools import reduce
from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)


n = int(input())
T = [int(input()) for _ in range(n)]

print(reduce(lcm, T))