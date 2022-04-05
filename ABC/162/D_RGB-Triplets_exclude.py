from functools import reduce
from operator import mul

n = int(input())
S = input()

num = list(map(S.count, 'RGB'))
ans = reduce(mul, num)

for l in range(n):
    for mid in range(l + 1, n):
        if S[l] == S[mid]:
            continue

        r = mid + mid - l
        if r < n and S[r] not in (S[l], S[mid]):
            ans -= 1

print(ans)