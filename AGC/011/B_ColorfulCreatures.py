from itertools import accumulate
n = int(input())
a = list(map(int, input().split()))
a.sort()
ac = list(accumulate(a))
a.extend([-float('inf')])

cnt = 0
for i in range(n):
    if ac[i] * 2 < a[i + 1]:
        cnt = 0
    else:
        cnt += 1
print(cnt)