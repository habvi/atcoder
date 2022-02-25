from collections import Counter

n = int(input())
A = list(map(int, input().split()))

mx = max(A)
mul = [0] * (mx + 1)
for a in set(A):
    for i in range(a * 2, mx + 1, a):
        mul[i] = 1

c = Counter(A)

ans = 0
for a in A:
    ans += (mul[a] == 0 and c[a] == 1)
print(ans)