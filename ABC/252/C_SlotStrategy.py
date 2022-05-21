n = int(input())

ts = [[0] * 10 for _ in range(10)]
for _ in range(n):
    S = input()
    for i, s in enumerate(S):
        s = int(s)
        ts[s][i] += 1

ans = float('inf')
for t in ts:
    mx = max(t)
    idx = -1
    for i, x in enumerate(t):
        if x == mx:
            idx = i
    ans = min(ans, (t[idx] - 1) * 10 + idx)
print(ans)