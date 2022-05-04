from math import gcd

n = int(input())
K, M = map(int, input().split())

g = gcd(K, M)
num = M // g
if n % num == 0:
    print('Yes')
else:
    print('No')