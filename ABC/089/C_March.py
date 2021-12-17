from collections import defaultdict
from itertools import combinations
n = int(input())
cnt = defaultdict(int)
for _ in range(n):
    s = input()
    if s[0] in 'MARCH':
        cnt[s[0]] += 1

ans = 0
for c1, c2, c3 in combinations(cnt.values(), 3):
    ans += c1 * c2 * c3
print(ans)