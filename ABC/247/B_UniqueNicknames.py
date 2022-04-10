from collections import Counter

n = int(input())

c = Counter()
name = []
for _ in range(n):
    s, t = input().split()
    c[s] += 1
    c[t] += 1
    name.append((s, t))

num = 0
for s, t in name:
    if s == t:
        num += (c[s] == 2)
    else:
        num += (c[s] == 1 or c[t] == 1)

print('Yes' if num == n else 'No')