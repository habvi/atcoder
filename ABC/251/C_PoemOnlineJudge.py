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



# ---------------------------
N = int(input())

used = set()
mx = 0
ans = None
for i in range(N):
    s, t = input().split()
    t = int(t)
    if s in used:
        continue
    used.add(s)
    if t > mx:
        ans = i + 1
        mx = t
print(ans)
