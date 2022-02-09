n, m = map(int, input().split())
X = list(map(int, input().split()))
X.sort()

dst = []
for i in range(m - 1):
    dst.append(X[i + 1] - X[i])

dst.sort()
for _ in range(n - 1):
    if dst:
        dst.pop()
print(sum(dst))