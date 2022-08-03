from collections import defaultdict

N, M = map(int, input().split())

q = defaultdict(int)
ac, wa = 0, 0
for _ in range(M):
    p, S = input().split()
    p = int(p)
    if q[p] != -1:
        if S == "WA":
            q[p] += 1
        else:
            ac += 1
            wa += q[p]
            q[p] = -1
print(ac, wa)
