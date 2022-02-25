from collections import defaultdict, deque

def bfs(u):
    dst[u] = 0
    q = deque([u])
    while q:
        v = q.popleft()
        for nv in g[v]:
            if dst[nv] != -1:
                if dst[nv] == dst[v] + 1:
                    case[nv] += case[v]
                    case[nv] %= MOD
                continue
            dst[nv] = dst[v] + 1
            case[nv] = case[v]
            q.append(nv)


MOD = 10**9 + 7
n = int(input())
start, goal = map(lambda x: int(x) - 1, input().split())

g = defaultdict(list)

m = int(input())
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append(b)
    g[b].append(a)


dst = [-1] * n
case = [0] * n
case[start] = 1
bfs(start)

print(case[goal] % MOD)