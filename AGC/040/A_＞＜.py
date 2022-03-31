from itertools import groupby

def sigma(n):
    return n * (n + 1) // 2


S = input()

his = []
for k, v in groupby(S):
    his.append((k, len(list(v))))

if his[0][0] == '>':
    his = [('<', 0), *his]

if his[-1][0] == '<':
    his.append(('>', 0))

ans = 0
for i in range(0, len(his), 2):
    _, l = his[i]
    _, r = his[i + 1]

    ans += sigma(l) + sigma(r)
    ans -= min(l, r)

print(ans)