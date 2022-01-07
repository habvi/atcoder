from itertools import combinations
a = list(map(int, input().split()))
ans = set()
for c in combinations(a, 3):
    ans.add(sum(c))
print(sorted(ans)[-3])