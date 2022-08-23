from collections import Counter

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(lambda x: int(x) - 1, input().split()))

ca = Counter(A)
cb = Counter()
for c in C:
    cb[B[c]] += 1

ans = 0
for a, v in ca.items():
    ans += v * cb[a]
print(ans)