N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())
h = Q - P + 1
w = S - R + 1
d = []
l1 = max(1 - A, 1 - B)
r1 = min(N - A, N - B)
l2 = max(1 - A, B - N)
r2 = min(N - A, B - 1)
for i in range(max(l1, P - A, R - B), min(r1, Q - A, S - B) + 1):
    d.append((A + i, B + i))
for i in range(max(l2, P - A, B - S), min(r2, Q - A, B - R) + 1):
    d.append((A + i, B - i))

g = [['.'] * w for _ in range(h)]
for i, j in d:
    g[i - P][j - R] = "#"

for gg in g:
    print(''.join(gg))