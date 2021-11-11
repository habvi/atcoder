from collections import deque
def bfs(u):
    seen = [0 for _ in range(n+1)]
    seen[u] = 1
    que = deque([])
    que.append(u)
    while que:
        v = que.popleft()
        for nv in A[v-1]:
            if seen[nv]: continue
            seen[nv] = 1
            ans[0] += tm[nv-1]
            que.append(nv)
    return

n = int(input())
tm = []
A = []
for _ in range(n):
    a = list(map(int, input().split()))
    tm.append(a[0])
    A.append(tuple(a[2:]))
    
ans = [tm[-1]]
bfs(n)
print(ans[0])