import sys
sys.setrecursionlimit(10 ** 7)

def dfs(x, total):
    if len(str(x)) > len_:
        return
    if x + total == n:
        ans.append(x)
        return

    for i in range(10):
        if x*10 + i == 0:
            continue
        dfs(x*10 + i, total + i)


n = int(input())

len_ = len(str(n))
ans = []
dfs(0, 0)

print(len(ans))
for num in sorted(ans):
    print(num)