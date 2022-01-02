from itertools import product
n = input()
k = len(n)
ans = float('inf')
for pr in product((0, 1), repeat=k):
    tot = 0
    erase = 0
    for i, p in enumerate(pr):
        if p:
           tot += int(n[i])
        else:
            erase += 1
    if tot % 3 == 0:
        ans = min(ans, erase)
print(ans if ans != k else -1)