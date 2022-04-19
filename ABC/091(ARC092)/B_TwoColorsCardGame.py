from collections import Counter

n = int(input())
c = Counter()
for _ in range(n):
    c[input()] += 1

m = int(input())
for _ in range(m):
    c[input()] -= 1

print(max(0, max(c.values())))