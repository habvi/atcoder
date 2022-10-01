N, S = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(N)]

INF = float('inf')
dp = [0] * (S + 1)
dp[0] = 1
his = [dp]
for a, b in ab:
    ndp = [0] * (S + 1)
    for i in range(S + 1):
        for x in (a, b):
            nxt = i + x
            if nxt <= S:
                ndp[nxt] |= dp[i]
    his.append(ndp)
    dp = ndp

if not his[-1][-1]:
    print("No")
    exit()

ans = []
now = S
for i, (a, b) in zip(reversed(range(N)), ab[::-1]):
    pre = now - a
    if pre >= 0 and his[i][pre]:
        now = pre
        ans.append('H')
        continue
    pre = now - b
    now = pre
    ans.append('T')
print("Yes")
print(''.join(ans[::-1]))