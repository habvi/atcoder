from collections import defaultdict

n = int(input())

d = defaultdict(lambda : defaultdict(int))
max_num = defaultdict(int)

pe = []
for _ in range(n):
    m = int(input())
    pe.append([tuple(map(int, input().split())) for _ in range(m)])
    for p, e in pe[-1]:
        d[p][e] += 1
        max_num[p] = max(max_num[p], e)

kind = set()
plus = 0
for i in range(n):
    t = []
    for p, e in pe[i]:
        if max_num[p] == e and d[p][e] == 1:
            t.append(p)
    if t:
        kind.add(tuple(sorted(t)))
    else:
        plus = 1

ans = len(kind) + plus
print(ans)