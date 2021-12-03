from collections import defaultdict
n = int(input())
k = len(str(n))
d = defaultdict(list)
for i in range(1, n + 1):
    f = str(i)[0]
    b = str(i)[-1]
    if f == 0 or b == 0:
        continue
    d[(int(f), int(b))].append(i)

ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        if (i, j) in d and (j, i) in d:
            ans += len(d[(i, j)]) * len(d[(j, i)])
print(ans)