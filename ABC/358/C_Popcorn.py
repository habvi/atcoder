N, M = map(int, input().split())
S = [input() for _ in range(N)]

INF = float("inf")
ans = INF
for i in range(1 << N):
    buy = set()
    for j in range(N):
        if (i >> j) & 1:
            for k, s in enumerate(S[j]):
                if s == "o":
                    buy.add(k)
    if len(buy) == M:
        ans = min(ans, bin(i).count("1"))

print(ans)
