from math import gcd

L, R = map(int, input().split())
d = R - L

while d:
    for i in range(R - L - d + 1):
        if gcd(L + i, L + i + d) == 1:
            print(d)
            exit()
    d -= 1