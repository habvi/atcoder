N, M = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(M)]
K = int(input())
cd = [tuple(map(int, input().split())) for _ in range(K)]

ans = 0
for bit in range(1 << K):
    ball = set()
    for i, (c, d) in enumerate(cd):
        if bit >> i & 1:
            ball.add(c)
        else:
            ball.add(d)
    total = 0
    for a, b in ab:
        total += (a in ball) and (b in ball)
    ans = max(ans, total)
print(ans)