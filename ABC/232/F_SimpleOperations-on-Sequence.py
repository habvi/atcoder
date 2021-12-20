def popcnt(x):
    x = x - ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 0x0000007f

n, x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
n2 = 1 << n
dp = [float('inf')] * n2
dp[0] = 0
for s in range(n2):
    j = popcnt(s)
    for i in range(n):
        if (s >> i)&1:
            continue
        cost = abs(a[i] - b[j]) * x
        cost += popcnt(s >> i) * y
        dp[s | (1<<i)] = min(dp[s | (1<<i)], dp[s] + cost)
ans = dp[n2 - 1]
print(ans)