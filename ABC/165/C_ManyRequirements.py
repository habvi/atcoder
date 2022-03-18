from itertools import combinations_with_replacement

n, m, q = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(q)]

ans = 0
for com in combinations_with_replacement(range(1, m + 1), n):
    total = 0
    for a, b, c, d  in A:
        a, b = a - 1, b - 1
        total += (d if com[b] - com[a] == c else 0)

    ans = max(ans, total)
print(ans)