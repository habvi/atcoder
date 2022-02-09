from collections import defaultdict

def get_cand(A, B):
    for x1, y1, i in A:
        for x2, y2, j in B:
            if i == j:
                continue
            if i > j:
                cand[(j, i)] = max(cand[(j, i)], max(abs(x1 - x2), abs(y1 - y2)))
            else:
                cand[(i, j)] = max(cand[(i, j)], max(abs(x1 - x2), abs(y1 - y2)))


n = int(input())
P = []
for i in range(n):
    x, y = map(int, input().split())
    P.append((x, y, i))

cand = defaultdict(int)

P.sort(key=lambda x: x[0])
get_cand(P[:5], P[-5:][::-1])

P.sort(key=lambda x: x[1])
get_cand(P[:5], P[-5:][::-1])

print(sorted(cand.values())[-2])