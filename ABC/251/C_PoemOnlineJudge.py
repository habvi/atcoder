from collections import defaultdict

n = int(input())

idx = defaultdict(lambda : (0, 0))
for i in range(n):
    s, t = input().split()
    t = int(t)
    if idx[s] == (0, 0):
        idx[s] = (t, i + 1)

score = list(idx.values())
score.sort(key=lambda x: (-x[0], x[1]))
print(score[0][1])