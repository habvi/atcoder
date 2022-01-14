from itertools import combinations_with_replacement
n, m, q = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(q)]
s = set()
for com in combinations_with_replacement(range(1, m + 1), n):
    s.add(tuple(sorted(com)))

ans = 0
for p in s:
    tot = 0
    for a, b, c, d in A:
        if p[b - 1] - p[a - 1] == c:
            tot += d
    ans = max(ans, tot)
print(ans)