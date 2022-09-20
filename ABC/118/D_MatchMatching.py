N, M = map(int, input().split())
A = set(map(int, input().split()))

match = [None, 2, 5, 5, 4, 5, 6, 3, 7, 6]

if (2 in A) and (3 in A) or (2 in A) and (5 in A):
    A.remove(2)
if (3 in A) and (5 in A):
    A.remove(3)
if (6 in A) and (9 in A):
    A.remove(6)

INF = float('inf')
dp = [-INF] * (N + 1)
dp[0] = 0
for a in sorted(A, reverse=True):
    for i in range(N + 1):
        pre = i - match[a]
        if pre >= 0:
            dp[i] = max(dp[i], dp[pre] * 10 + a)
print(dp[-1])