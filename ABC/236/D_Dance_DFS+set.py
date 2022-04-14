import sys
sys.setrecursionlimit(10**7)

def dfs(first, xor, seen):
    if len(seen) == n2:
        global ans
        ans = max(ans, xor)
        return

    if len(seen) % 2:
        for second in range(n2):
            if second not in seen:
                seen.add(second)
                dfs(None, xor ^ A[first][second], seen)
                seen.remove(second)
    else:
        for first in range(n2):
            if first not in seen:
                seen.add(first)
                dfs(first, xor, seen)
                break
        seen.remove(first)


n = int(input())
n2 = 2 * n

A = [[-1] * n2 for _ in range(n2)]
for i in range(n2 - 1):
    A[i][i + 1:] = map(int, input().split())

ans = 0
dfs(None, 0, set())
print(ans)