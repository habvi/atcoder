from itertools import product
s = input()
n = len(s)
ans = 20
for pr in product([0, 1], repeat=n):
    a = 0
    cnt = 0
    for i, p in enumerate(pr):
        if p: a += int(s[i])
        else: cnt += 1

    if a % 3 == 0 and a != 0:
        ans = min(ans, cnt)
print(ans if ans != 20 else -1)