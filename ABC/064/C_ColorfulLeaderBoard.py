from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))

num = defaultdict(int)
for a in A:
    if a >= 3200:
        num[8] += 1
    else:
        num[a // 400] = 1

m = len(num)
if not (free := num[8]):
    print(m, m)
else:
    fixed = m - 1
    print(max(1, fixed), fixed + free)