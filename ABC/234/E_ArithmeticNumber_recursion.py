from bisect import bisect_left

def dfs(x, diff):
    if len(str(x)) > n + 1:
        return
    cand.add(x)

    t = x % 10
    x *= 10
    if 0 <= t + diff <= 9:
        dfs(x + t + diff, diff)


X = int(input())
n = len(str(X))

cand = set()
for x in range(1, 10):
    for diff in range(-9, 10):
        dfs(x, diff)

cand = sorted(cand)
bi = bisect_left(cand, X)
print(cand[bi])