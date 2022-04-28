from collections import defaultdict

h, w = map(int, input().split())
S = [input() for _ in range(h)]
MOD = 998244353

kind = defaultdict(set)
for i in range(h):
    for j in range(w):
        kind[i + j].add(S[i][j])

ans = 1
for k, v in kind.items():
    if 'B' in v and 'R' in v:
        print(0)
        exit()

    if v == {'.'}:
        ans *= 2
        ans %= MOD
print(ans)