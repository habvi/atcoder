from collections import defaultdict

S = input()

d = defaultdict(int)
d[0] += 1
total = 0
ans = 0
for s in S:
    x = int(s)
    total ^= (1 << x)
    ans += d[total]
    d[total] += 1
print(ans)
