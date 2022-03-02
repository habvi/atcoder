def dfs(mul, i):
    global ans
    if i == n:
        ans += mul == x
        return

    for a in A[i]:
        dfs(mul * a, i + 1)


n, x = map(int, input().split())
A = []
for _ in range(n):
    L, *a = map(int, input().split())
    A.append(a)

ans = 0
dfs(1, 0)

print(ans)