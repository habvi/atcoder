N, M = map(int, input().split())

s = set()
ans = 0
for _ in range(M):
    u, v = map(lambda x: int(x) - 1, input().split())
    if (u, v) in s or (v, u) in s or u == v:
        ans += 1
        continue
    s.add((u, v))
print(ans)
