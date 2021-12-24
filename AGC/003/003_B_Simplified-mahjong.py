from itertools import groupby
n = int(input())
a = [int (input()) for _ in range(n)] + [0]

ans = 0
cnt = 0
for k, v in groupby(a):
    if k:
        cnt += sum(list(v))
    else:
        ans += cnt // 2
        cnt = 0
print(ans)