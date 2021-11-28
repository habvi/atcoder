from itertools import groupby
n = int(input())
s = input()
ans = 0
for k, g in groupby(s):
    l = len(list(g))
    if l > 1:
        ans += (l * (l - 1) // 2)
print(ans)