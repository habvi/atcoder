def dfs(x):
    global ans
    if x:
        ans += (len(set(x)) >= 3 and int(x) <= n)
        if len(x) == m:
            return

    for i in (3, 5, 7):
        dfs(x + str(i))


n = int(input())
m = len(str(n))
ans = 0
dfs('')

print(ans)