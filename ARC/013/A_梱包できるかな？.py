from itertools import permutations

n, m, l = map(int, input().split())
p, q, r = map(int, input().split())

ans = 0
for a, b, c in permutations((p, q, r)):
    ans = max(ans, (n//a) * (m//b) * (l//c))

print(ans)