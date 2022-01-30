from itertools import groupby, accumulate

S = input()
n = len(S)

S = S.replace('25', 'X')
ac = list(accumulate(range(n + 1)))

ans = 0
for k, g in groupby(S):
    if k == 'X':
        ans += ac[len(list(g))]
print(ans)