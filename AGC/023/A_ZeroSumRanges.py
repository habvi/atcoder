from itertools import accumulate
from collections import Counter
n = int(input())
A = list(map(int, input().split()))
ac = [0] + list(accumulate(A))

c = Counter(ac)

ans = 0
for v in c.values():
    ans += (v * (v-1) // 2)
print(ans)