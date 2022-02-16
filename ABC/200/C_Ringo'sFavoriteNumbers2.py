from collections import Counter

def comb(x):
    return x * (x - 1) // 2


n = int(input())
A = list(map(int, input().split()))

A = [a % 200 for a in A]

ans = 0
for v in Counter(A).values():
    ans += comb(v)
print(ans)