n, m, q = map(int, input().split())
G = [[] for _ in range(n)]
for i in range(m):
    u, v = map(int, input().split())
    u, v = u-1, v-1
    G[u].append(v)
    G[v].append(u) 

c = list(map(int, input().split()))
for _ in range(q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        x = s[1]-1
        print(c[x])
        for g in G[x]:
            c[g] = c[x]
    else:
        x, y = s[1]-1, s[2]
        print(c[x])
        c[x] = y