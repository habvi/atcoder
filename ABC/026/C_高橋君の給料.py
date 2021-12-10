from collections import defaultdict
n = int(input())
d = defaultdict(list)
for i in range(2, n + 1):
    a = int(input())
    d[a].append(i)

s = [0] * (n + 1)
for i in range(n, 0, -1):
    if i not in d:
        s[i] = 1
        continue
    mx, mn = 0, float('inf')
    for j in d[i]:
        mx = max(mx, s[j])
        mn = min(mn, s[j])
    s[i] = mx + mn + 1
print(s[1])