import sys
sys.setrecursionlimit(10 ** 7)

DXY = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dfs(S):
    global ans
    red = 0
    for y in range(n):
        for x in range(n):
            red += (S[y][x] == '@')
    if red == K:
        ans += 1
        return

    for y in range(n):
        for x in range(n):
            if S[y][x] != '.':
                continue

            if red:
                ok = False
                for dy, dx in DXY:
                    ny, nx = y + dy, x + dx
                    if not (0 <= ny < n and 0 <= nx < n):
                        continue
                    if S[ny][nx] == '@':
                        ok = True
                        break
                if not ok:
                    continue

            S[y][x] = '@'
            dfs(S)
            S[y][x] = '#'
            dfs(S)
            S[y][x] = '.'
            return


n = int(input())
K = int(input())
S = [list(input()) for _ in range(n)]

ans = 0
dfs(S)
print(ans)