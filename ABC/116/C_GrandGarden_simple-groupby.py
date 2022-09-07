from itertools import groupby

N = int(input())
H = list(map(int, input().split()))

mx = max(H)
ans = 0
for x in reversed(range(1, mx + 1)):
    for k, _ in groupby(H):
        ans += (k == x)
    for i in range(N):
        if H[i] == x:
            H[i] -= 1
print(ans)
