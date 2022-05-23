from heapq import heapify, heappop, heappush

n, L = map(int, input().split())
A = list(map(int, input().split()))

hq = A[:]
heapify(hq)

if (res := L - sum(A)) > 0:
    heappush(hq, res)

ans = 0
while len(hq) != 1:
    a = heappop(hq)
    b = heappop(hq)
    ans += a + b
    heappush(hq, a + b)

print(ans)