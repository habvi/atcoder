def dfs(seen, xor):
    global ans
    if seen == (1 << n2) - 1:
        ans = max(ans, xor)
        return

    for first in range(n2):
        if not seen >> first & 1:
            seen |= 1 << first
            break

    for second in range(n2):
        if not seen >> second & 1:
            dfs(seen | 1 << second, xor ^ A[first][second])


n = int(input())
n2 = n * 2
A = [[0] * n2 for _ in range(n2)]

for i in range(n2 - 1):
    A[i][i + 1:] = map(int, input().split())

ans = 0
dfs(0, 0)
print(ans)