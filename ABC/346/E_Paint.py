from collections import defaultdict

H, W, M = map(int, input().split())
q = [tuple(map(int, input().split())) for _ in range(M)]

zan_h = H
zan_w = W
num = defaultdict(int)
used_h = set()
used_w = set()
for t, a, x in q[::-1]:
    a -= 1
    if t == 1:
        if not a in used_h:
            num[x] += zan_w
            zan_h -= 1
            used_h.add(a)
    else:
        if not a in used_w:
            num[x] += zan_h
            zan_w -= 1
            used_w.add(a)

num[0] += zan_h * zan_w
ans = []
for k in sorted(num.keys()):
    if num[k]:
        ans.append((k, num[k]))

print(len(ans))
for a, b in ans:
    print(a, b)
