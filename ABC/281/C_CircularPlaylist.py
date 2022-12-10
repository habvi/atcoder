from itertools import accumulate
from bisect import bisect

N, T = map(int, input().split())
A = list(map(int, input().split()))

ac = [0] + list(accumulate(A))
mod = T % ac[-1]
bi = bisect(ac, mod)
print(bi, mod - ac[bi - 1])