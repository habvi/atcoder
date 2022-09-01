from collections import Counter

N = int(input())
A = list(map(int, input().split()))

c = Counter(A)
mx = max(A)
for a in set(A):
    for i in range(2 * a, mx + 1, a):
        c[i] = 0

ans = 0
for a in A:
    ans += (c[a] == 1)
print(ans)