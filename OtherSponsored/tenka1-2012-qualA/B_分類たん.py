from itertools import groupby

S = input()

ans = []
for k, g in groupby(S):
    if k == ' ':
        ans.append(',')
    else:
        ans.append(k * len(list(g)))
print(''.join(ans))