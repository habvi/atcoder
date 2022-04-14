import sys
sys.setrecursionlimit(10**7)

def dfs(a):
    global ans
    if len(a) == n2:
        xor = 0
        for i in range(0, n2, 2):
            xor ^= d[a[i]][a[i + 1]]
        ans = max(ans, xor)
        return

    if len(a) % 2:
        for i in range(n2):
            if i not in a:
                a.append(i)
                dfs(a)
                a.pop()
    else:
        for i in range(n2):
            if i not in a:
                a.append(i)
                dfs(a)
                break
        a.pop()


n = int(input())
n2 = 2 * n

A = []
for _ in range(n2 - 1):
    a = list(map(int, input().split()))
    A.extend(a)

d = [[-1] * n2 for _ in range(n2)]
k = 0
for i in range(n2):
    for j in range(i + 1, n2):
        d[i][j] = A[k]
        k += 1

ans = 0
dfs([])
print(ans)