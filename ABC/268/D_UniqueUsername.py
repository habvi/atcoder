from collections import defaultdict
from itertools import groupby, permutations

N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = set(input() for _ in range(M))

if N == 1:
    print(S[0] if S[0] not in T and len(S[0]) >= 3 else -1)
    exit()

d = defaultdict(set)
for t in T:
    if t[0] == '_' or t[-1] == '_':
        continue
    ws = []
    ub = []
    w = ""
    for k, v in groupby(t):
        lv = len(list(v))
        if k != '_':
            w += k * lv
        else:
            ws.append(w)
            ub.append(lv)
            w = ""
    if w:
        ws.append(w)
    d[tuple(ws)].add(tuple(ub))

def dfs(A):
    if len(A) == N - 1:
        if sum(A) <= ub_total:
            ub_all.append(tuple(A))
        return
    for i in range(1, ub_total):
        dfs(A + [i])

ub_total = 16 - sum(map(len, S))
ub_all = []
for i in range(1, ub_total + 1):
    dfs([i])

for per in permutations(S):
    for ub in ub_all:
        if ub not in d[per]:
            ans = ""
            for w, u in zip(per, list(ub) + [0]):
                ans += w + '_' * u
            print(ans)
            exit()
print(-1)