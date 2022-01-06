from collections import defaultdict
n, m = map(int, input().split())
ac = set()
wa = defaultdict(int)
for _ in range(m):
    p, s = input().split()
    p = int(p)
    if p in ac:
        continue
    if s == 'AC':
        ac.add(p)
    else:
        wa[p] += 1

a, w = 0, 0
for i in range(1, n + 1):
    if i in ac:
        a += 1
        w += wa[i]
print(a, w)