from collections import defaultdict, deque

def is_ok(S):
    def bfs(u):
        seen = [0] * N
        seen[u] = 1
        que = deque([])
        que.append(u)
        while que:
            v = que.popleft()
            for nv in g[v]:
                if seen[nv]:
                    continue
                seen[nv] = 1
                que.append(nv)
        return sum(seen)

    g = defaultdict(set)
    for i in range(N):
        x1, y1, p1 = xyp[i]
        for j in range(i + 1, N):
            x2, y2, p2 = xyp[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            if p1 * S >= dist:
                g[i].add(j)
            if p2 * S >= dist:
                g[j].add(i)
    for v in range(N):
        if bfs(v) == N:
            return True
    return False

def bisect(ng, ok):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


N = int(input())
xyp = [tuple(map(int, input().split())) for _ in range(N)]

mx = 10 ** 10
ans = bisect(-1, mx)
print(ans)