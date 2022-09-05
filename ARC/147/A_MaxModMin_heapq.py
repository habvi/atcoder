from heapq import heapify, heappop, heappush

N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
mn = A.pop()
hq = [-a for a in A]
heapify(hq)

ans = 0
while hq:
    mx = -heappop(hq)
    mx %= mn
    ans += 1
    if not mx:
        continue
    heappush(hq, -mn)
    mn = mx
print(ans)
