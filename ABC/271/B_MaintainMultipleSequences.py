N, Q = map(int, input().split())
L = []
for _ in range(N):
    _, *l = tuple(map(int, input().split()))
    L.append(l)

for _ in range(Q):
    s, t = map(lambda x: int(x) - 1, input().split())
    print(L[s][t])