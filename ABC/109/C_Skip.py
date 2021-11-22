from math import gcd
n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans = gcd(ans, abs(x - a[i]))
print(ans)