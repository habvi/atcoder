n, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ab = []
for i, (a, b) in enumerate(zip(A, B)):
    ab.append((i + 1, a, b, a + b))

ans = []
ab.sort(key=lambda x: (x[1], -x[0]))
for _ in range(X):
    ans.append(ab.pop()[0])

ab.sort(key=lambda x: (x[2], -x[0]))
for _ in range(Y):
    ans.append(ab.pop()[0])

ab.sort(key=lambda x: (x[3], -x[0]))
for _ in range(Z):
    ans.append(ab.pop()[0])

ans.sort()
print(*ans)