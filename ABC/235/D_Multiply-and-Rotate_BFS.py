from collections import deque, defaultdict
def bfs(u):
    dst = defaultdict(lambda : -1)
    dst[u] = 0
    q = deque([u])
    while q:
        v = q.popleft()
        nv = v * a
        if len(str(nv)) <= n and dst[nv] == -1:
            dst[nv] = dst[v] + 1
            q.append(nv)
        if v >= 10 and v % 10:
            sv = str(v)
            nv = int(sv[-1] + sv[:-1])
            if len(str(nv)) <= n and dst[nv] == -1:
                dst[nv] = dst[v] + 1
                q.append(nv)
    return dst

a, s = input().split()
a = int(a)
n = len(s)
dst = bfs(1)
print(dst[int(s)])