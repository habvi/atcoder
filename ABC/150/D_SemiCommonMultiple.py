from math import gcd

def ceil(a, b):
    return (a + b - 1) // b

def lcm(a, b):
    return a * b // gcd(a, b)


n, m = map(int, input().split())
A = list(map(int, input().split()))

A = set(A)
B = []
kind = set()
for a in A:
    B.append(a // 2)
    times = 0
    while a % 2 == 0:
        a //= 2
        times += 1
    kind.add(times)

if len(kind) != 1:
    print(0)
    exit()

mul = B[0]
for b in B:
    mul = lcm(mul, b)
    if mul > m:
        print(0)
        exit()

print(ceil(m // mul, 2))