from heapq import heappop, heappush

n = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

hq = []
for i, t in enumerate(T):
    heappush(hq, (t, i))

ans = [None] * n
num = 0
while num < n:
    t, i = heappop(hq)
    if ans[i] is None:
        ans[i] = t
        heappush(hq, (t + S[i], (i + 1) % n))
        num += 1

print(*ans)