from collections import defaultdict

n, m = map(int, input().split())

INF = float('inf')
box = defaultdict(lambda : INF)
for _ in range(m):
    a, b = map(int, input().split())
    C = list(map(lambda x: int(x) - 1, input().split()))

    s = 0
    for c in C:
        s |= 1 << c
    box[s] = min(box[s], a)

dp = [INF] * (1 << n)
dp[0] = 0
for k, v in box.items():
    for pre in reversed(range(1 << n)):
        nxt = pre | k
        dp[nxt] = min(dp[nxt], dp[pre] + v)

print(dp[-1] if dp[-1] != INF else -1)