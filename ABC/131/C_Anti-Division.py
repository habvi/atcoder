from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)


a, b, c, d = map(int, input().split())

total = b - a + 1
total -= (b // c - (a - 1) // c)
total -= (b // d - (a - 1) // d)

x = lcm(c, d)
total += (b // x - (a - 1) // x)
print(total)