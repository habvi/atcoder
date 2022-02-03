from itertools import accumulate

def sigma(x):
    return x * (x + 1) // 2


n, K = map(int, input().split())
P = list(map(int, input().split()))

exp = []
for p in P:
    exp.append(sigma(p) / p)

ac = [0, *accumulate(exp)]

ans = 0
for i in range(K, n + 1):
    ans = max(ans, ac[i] - ac[i - K])
print(ans)