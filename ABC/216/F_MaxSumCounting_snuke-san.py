n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
MOD = 998244353

ab = []
for a, b in zip(A, B):
    ab.append((a, b))
ab.sort()

mx = max(A)
dp = [1] * (mx + 1)
ans = 0
for a, b in ab:
    if a >= b:
        ans += dp[a - b]
    for i in reversed(range(mx + 1)):
        nxt = i + b
        if nxt <= mx:
            dp[nxt] += dp[i]
            dp[nxt] %= MOD
    ans %= MOD

print(ans)