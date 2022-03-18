h, w, n = map(int, input().split())
y, x = set(), set()
ab = []
for i in range(n):
    a, b = map(int, input().split())
    y.add(a)
    x.add(b)
    ab.append((a, b))

Y = {num : i for i, num in enumerate(sorted(y), 1)}
X = {num : i for i, num in enumerate(sorted(x), 1)}

for a, b in ab:
    print(Y[a], X[b])