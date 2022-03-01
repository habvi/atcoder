from itertools import accumulate
n = int(input())
a = list(map(int, input().split()))
ac = list(accumulate(a))

sm = ac[-1]
ans = float('inf')
for i in range(n - 1):
    ans = min(ans, abs(sm - ac[i] - ac[i]))
print(ans)