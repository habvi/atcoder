from bisect import bisect

n, k = map(int, input().split())
P = [tuple(map(int, input().split())) for _ in range(n)]

score = [sum(p) for p in P]
ss = sorted(score)

for s in score:
    if n - bisect(ss, s + 300) + 1 <= k:
        print('Yes')
    else:
        print('No')