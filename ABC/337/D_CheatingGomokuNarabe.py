from collections import deque

INF = float('inf')

def calc(S):
    q = deque([])
    total_o = 0
    total_x = 0
    ans = INF
    for s in S:
        q.append(s)
        total_o += (s == 'o')
        total_x += (s == 'x')

        while q and (total_x or len(q) > K):
            rm = q.popleft()
            total_o -= (rm == 'o')
            total_x -= (rm == 'x')

        if len(q) == K:
            ans = min(ans, K - total_o)
    return ans


H, W, K = map(int, input().split())
S = [input() for _ in range(H)]

mn = INF
# row
for s in S:
    mn = min(mn, calc(s))
# col
for s in zip(*S):
    mn = min(mn, calc(s))

print(mn if mn != INF else -1)