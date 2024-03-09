from collections import defaultdict

T = input()
N = int(input())

INF = float('inf')
dp = defaultdict(lambda : INF)
dp[""] = 0

for _ in range(N):
    A = input().split()
    m = int(A[0])
    S = A[1:]

    ndp = defaultdict(lambda : INF)
    ndp[""] = 0
    for s in S:
        for ps, pnum in dp.items():
            ndp[ps] = min(ndp[ps], pnum)
            ns = ps + s
            if ns in T:
                ndp[ns] = min(ndp[ns], pnum + 1)
    dp = ndp

print(dp[T] if dp[T] != INF else -1)
