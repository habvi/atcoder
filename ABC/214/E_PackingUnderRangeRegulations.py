from heapq import heappop, heappush

def solve():
    n = int(input())
    lr = [tuple(map(int, input().split())) for _ in range(n)]
    lr.append((INF, INF))

    lr.sort()
    hq = []
    now = 1
    for l, r in lr:
        while hq and now < l:
            if now > hq[0]:
                print('No')
                return
            heappop(hq)
            now += 1
        now = l
        heappush(hq, r)
    print('Yes')


T = int(input())
INF = float('inf')
for _ in range(T):
    solve()