from itertools import accumulate

n, C = map(int, input().split())
stc = [tuple(map(int, input().split())) for _ in range(n)]

stc.sort(key=lambda x: (x[2], x[0]))

ch = [[] for _ in range(30)]
for s, t, c in stc:
    c -= 1
    if not ch[c]:
        ch[c].append([s - 1, t])
    else:
        if ch[c][-1][1] in (s, s - 1):
            ch[c][-1][1] = t
        else:
            ch[c].append([s - 1, t])

mx = 10 ** 5
num = [0] * (mx + 1)
for st in ch:
    for s, t in st:
        num[s] += 1
        num[t] -= 1

ac = list(accumulate(num))
print(max(ac))