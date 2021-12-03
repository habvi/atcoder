from collections import deque
n, D = map(int, input().split())
a = [tuple(map(int, input().split())) for _ in range(n)]
a.sort(key=lambda x : x[1])
d = deque(a)

_, r = d.popleft()
ans = 1
while d:
    nl, nr = d.popleft()
    if nl <= r + D - 1:
        pass
    else:
        r = nr
        ans += 1
print(ans)