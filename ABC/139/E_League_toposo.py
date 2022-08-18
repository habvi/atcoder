from collections import defaultdict, deque

def set_id(a, b):
    global num
    if a > b:
        a, b = b, a
    if ids[(a, b)] == -1:
        ids[(a, b)] = num
        num += 1

def get_id(a, b):
    if a > b:
        a, b = b, a
    return ids[(a, b)]


N = int(input())
g = defaultdict(list)
ids = defaultdict(lambda : -1)
in_deg = defaultdict(int)
num = 0
for a in range(N):
    B = list(map(lambda x: int(x) - 1, input().split()))
    for b in B:
        set_id(a, b)
    for j in range(N - 2):
        l = get_id(a, B[j])
        r = get_id(a, B[j + 1])
        g[l].append(r)
        in_deg[r] += 1

que = deque([])
dist = [0] * num
for v in range(num):
    if not in_deg[v]:
        que.append(v)
        dist[v] = 1

toposo = []
while que:
    v = que.pop()
    toposo.append(v)
    for nv in g[v]:
        in_deg[nv] -= 1
        dist[nv] = max(dist[nv], dist[v] + 1)
        if not in_deg[nv]:
            que.append(nv)
print(max(dist) if len(toposo) == num else -1)