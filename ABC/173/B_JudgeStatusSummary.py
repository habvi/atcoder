from collections import Counter

n = int(input())
S = [input() for _ in range(n)]

c = Counter(S)
for s in ('AC', 'WA', 'TLE', 'RE'):
    print(f'{s} x {c[s]}')