from collections import defaultdict

N, M = map(int, input().split())
A, B, C, D, E, F = map(int, input().split())
ng = set()
for _ in range(M):
    x, y = map(int, input().split())
    ng.add((x, y))
MOD = 998244353

dp = defaultdict(int)
dp[(0, 0)] = 1
for _ in range(N):
    ndp = defaultdict(int)
    for (x, y), v in dp.items():
        for dx, dy in ((A, B), (C, D), (E, F)):
            nx, ny = x + dx, y + dy
            if (nx, ny) not in ng:
                ndp[(nx, ny)] += (v % MOD)
    dp = ndp
ans = sum(dp.values()) % MOD
print(ans)



# --------------------------------------
# faster
from collections import defaultdict

N, M = map(int, input().split())
A, B, C, D, E, F = map(int, input().split())
ng = set()
for _ in range(M):
    x, y = map(int, input().split())
    ng.add((x, y))
MOD = 998244353

dp = defaultdict(int)
dp[(0, 0)] = 1
for _ in range(N):
    ndp = defaultdict(int)
    for (x, y), v in dp.items():
        nx, ny = x + A, y + B
        if (nx, ny) not in ng:
            ndp[(nx, ny)] += (v % MOD)
        nx, ny = x + C, y + D
        if (nx, ny) not in ng:
            ndp[(nx, ny)] += (v % MOD)
        nx, ny = x + E, y + F
        if (nx, ny) not in ng:
            ndp[(nx, ny)] += (v % MOD)
    dp = ndp
ans = sum(dp.values()) % MOD
print(ans)