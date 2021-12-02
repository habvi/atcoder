import sys
sys.setrecursionlimit(10 ** 7)
def f(i, j):
    if i == h - 1 and j == w - 1:
        return 0
    if seen[i][j]:
        return memo[i][j]
    seen[i][j] = True
    res = -float('inf')
    if i + 1 < h:
        res = max(res, (1 if s[i + 1][j] == '+' else -1) - f(i + 1, j))
    if j + 1 < w:
        res = max(res, (1 if s[i][j + 1] == '+' else -1) - f(i, j + 1))
    memo[i][j] = res
    return res

h, w = map(int, input().split())
s = [input() for _ in range(h)]
seen = [[False] * (w + 1) for _ in range(h + 1)]
memo = [[0] * (w +1) for _ in range(h + 1)]

score = f(0, 0)
if score == 0:
    print('Draw')
elif score < 0:
    print('Aoki')
else:
    print('Takahashi')