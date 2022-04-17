from collections import Counter

n, m = map(int, input().split())
A = list(map(int, input().split()))

c = Counter([0])
total = 0
ans = 0
for a in A:
    total = (total + a) % m
    ans += c[total]
    c[total] += 1

print(ans)