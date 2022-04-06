def dfs(x):
    if len(str(x)) >= 11:
        return
    s.append(x)

    t = x % 10
    if t - 1 >= 0:
        dfs(x * 10 + t - 1)

    dfs(x * 10 + t)

    if t + 1 <= 9:
        dfs(x * 10 + t + 1)


K = int(input())

s = []
for i in range(1, 10):
    dfs(i)
print(sorted(s)[K - 1])