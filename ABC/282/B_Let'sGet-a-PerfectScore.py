from itertools import combinations

N, M = map(int, input().split())
S = [input() for _ in range(N)]

ans = 0
for a, b in combinations(range(N), 2):
    total = 0
    for i, (sa, sb) in enumerate(zip(S[a], S[b])):
        if sa == 'o' or sb == 'o':
            total |= 1 << i
    ans += ((1 << M) - 1 == total)
print(ans)
