n, m = map(int, input().split())
c = [i + 1 for i in range(n)]
now = 0
for i in range(m):
    d = int(input())
    if d == now:
        continue
    c[c.index(d)] = now
    now = d
    
for ans in c:
    print(ans)