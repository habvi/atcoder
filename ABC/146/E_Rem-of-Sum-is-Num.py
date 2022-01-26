from collections import defaultdict

n, k = map(int, input().split())
A = list(map(lambda x: int(x) - 1, input().split()))
MOD = k

ac = [0]
for a in A:
    ac.append((ac[-1] + a) % MOD)

d = defaultdict(int)
tot = 0
ans = 0
for i, a in enumerate(ac):
    if tot == k:
        d[ac[i - k]] -= 1
        tot -= 1
    ans += d[a]
    d[a] += 1
    tot += 1
print(ans)