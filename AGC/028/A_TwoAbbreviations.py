# 3 5
# d . . n . . s . . u . . s . . r
# d . . . . u . . . . j . . . . r

from math import gcd
def lcm(a, b):
    return a * b // gcd(a, b)

n, m = map(int, input().split())
s = input()
t = input()
g = gcd(n, m)
a = n // g
b = m // g
x = []
for i in range(0, n, a):
    x.append(s[i])
y = []
for i in range(0, m, b):
    y.append(t[i])
print(lcm(n, m) if x == y else -1)