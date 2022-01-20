n, k = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))
seen = set()
loop = []
now = 0
for _ in range(n):
    seen.add(now)
    loop.append(now)
    now = A[now]
    if now in seen:
        break
    
idx = loop.index(now)
if k < idx:
    print(loop[k] + 1)
    exit()

print(loop[(k - idx) % (len(loop) - idx) + idx] + 1)