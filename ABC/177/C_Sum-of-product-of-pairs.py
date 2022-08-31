from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))
MOD = 10**9 + 7

ac = list(accumulate(A))
ans = 0
for i, a in enumerate(A):
    ans += a * (ac[-1] - ac[i])
    ans %= MOD
print(ans)

