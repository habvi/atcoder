from itertools import groupby

N, D = map(int, input().split())
S = [input() for _ in range(N)]

free = [0] * D
for i, x in enumerate(zip(*S)):
    if all(day == 'o' for day in x):
        free[i] = 1

ans = 0
for k, v in groupby(free):
    if k:
        ans = max(ans, len(list(v)))
print(ans)
