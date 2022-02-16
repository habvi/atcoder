from itertools import groupby

S = input()
T = 'ACGT'

S = ['x' if s in T else s for s in S]

ans = 0
for k, v in groupby(S):
    if k == 'x':
        ans = max(ans, len(list(v)))
print(ans)