from collections import defaultdict

def sigma(n):
    return n*(n + 1) // 2


n, C = map(int, input().split())
A = list(map(int, input().split()))

idx = defaultdict(list)
for i, a in enumerate(A):
    idx[a].append(i)

for i in range(1, C + 1):
    if idx[i]:
        idx[i] = [-1, *idx[i], n]

    ans = sigma(n)
    for j in range(len(idx[i]) - 1):
        l, r = idx[i][j], idx[i][j + 1]
        ans -= sigma(r - l - 1)
    print(ans)