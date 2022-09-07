from collections import Counter

n = int(input())
S = [input() for _ in range(n)]

c = Counter(S)
mx = c.most_common()[0][1]
for s in sorted(c.keys()):
    if c[s] == mx:
        print(s)