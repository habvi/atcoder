from heapq import heappop, heappush

n, K = map(int, input().split())

ty = [(1, 0)]
now = 0
for _ in range(n):
    t, y = map(int, input().split())
    ty.append((t, y))
    if t == 1:
        now = y
    else:
        now += y

ans = now
erase = []
plus = 0
k = 0
for t, y in ty[::-1]:
    if t == 1:
        while erase and len(erase) > K - k:
            rm = heappop(erase)
            plus += -rm

        ans = max(ans, y + plus)
        k += 1
        if k == K + 1:
            break
    else:
        if y < 0:
            heappush(erase, -y)
        else:
            plus += y
print(ans)