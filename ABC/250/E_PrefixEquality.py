from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

bis = defaultdict(list)
for i, b in enumerate(B):
    bis[b].append(i)

used_a = set()
used_bi = set()
yet_a = set()
idx = defaultdict(int)
now = -1
for i, a in enumerate(A, 1):
    if not bis[a]:
        break

    if a not in used_a:
        for bi in bis[a]:
            used_bi.add(bi)
        used_a.add(a)
        yet_a.add(a)

    if yet_a:
        left = -1

    while now + 1 in used_bi:
        rm = B[now + 1]
        if rm in yet_a:
            yet_a.remove(rm)
        if left == -1 and not yet_a:
            left = now + 1
        now += 1

    if not yet_a:
        idx[i] = (left + 1, now + 1)


Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    if not idx[x]:
        print('No')
        continue

    l, r = idx[x]
    if l <= y <= r:
        print('Yes')
    else:
        print('No')