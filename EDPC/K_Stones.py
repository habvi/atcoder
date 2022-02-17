n, k = map(int, input().split())
A = list(map(int, input().split()))

dp = [0] * (k + 1)

for i in range(1, k + 1):
    for a in A:
        if i - a  >= 0 and dp[i - a] == 0:
            dp[i] = 1

print('First' if dp[k] else 'Second')