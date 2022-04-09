from bisect import bisect_left

n = int(input())
L = list(map(int, input().split()))

L.sort()

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        total = L[i] + L[j]
        bi = bisect_left(L, total)
        ans += bi - 1 - j

print(ans)