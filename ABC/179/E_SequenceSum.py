n, x, MOD = map(int, input().split())

loop = [x]
seen = set()
seen.add(x)
for _ in range(MOD):
    m = loop[-1]**2 % MOD
    if m in seen:
        break
    seen.add(m)
    loop.append(m)

front = loop.index(m)
ans = sum(loop[:front])

loop = loop[front:]

n -= front
total = sum(loop)
lc = len(loop)

ans += total * (n // lc)
ans += sum(loop[:n % lc])
print(ans)