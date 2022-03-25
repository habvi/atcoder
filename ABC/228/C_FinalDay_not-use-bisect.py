n, k = map(int, input().split())
P = [tuple(map(int, input().split())) for _ in range(n)]

score = [sum(p) for p in P]
cmp = sorted(score)[-k]

for s in score:
    print('Yes' if s + 300 >= cmp else 'No')