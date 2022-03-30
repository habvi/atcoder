from collections import defaultdict, deque

def bfs(u):
    dist = [-1] * n
    dist[u] = 0
    q = deque([u])

    back = defaultdict(lambda : None)
    while q:
        v = q.popleft()
        for nv, ni in g[v]:
            if dist[nv] != -1:
                continue

            back[nv] = (v, ni)
            if nv == goal:
                break
            dist[nv] = dist[v] + 1
            q.append(nv)

    now = goal
    while now != start:
        now, ni = back[now]
        count_[ni] += 1


n, m, K = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))
MOD = 998244353

g = defaultdict(list)
for i in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].append((b, i))
    g[b].append((a, i))

count_ = [0] * (n - 1)
for i in range(m - 1):
    start, goal = A[i], A[i + 1]
    bfs(start)

total = sum(count_)
kt = K + total
if (total < K) or (kt % 2) or (kt < 0):
    print(0)
    exit()

R = kt // 2

dp = [0] * (R + 1)
dp[0] = 1
for num in count_:
    for i in reversed(range(R + 1)):
        if i + num <= R:
            dp[i + num] += dp[i]
            dp[i + num] %= MOD
print(dp[R])