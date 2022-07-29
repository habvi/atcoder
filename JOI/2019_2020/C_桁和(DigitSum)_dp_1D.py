def digit_sum(x):
    return sum(int(d) for d in str(x))


N = int(input())

dp = [0] * (N + 1)
dp[N] = 1
for x in reversed(range(1, N)):
    nxt = x + digit_sum(x)
    if nxt <= N and dp[nxt]:
        dp[x] = 1
print(sum(dp))