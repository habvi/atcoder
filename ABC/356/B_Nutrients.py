N, M = map(int, input().split())
A = list(map(int, input().split()))

total = [0] * M
for _ in range(N):
    X = list(map(int, input().split()))
    for i, x in enumerate(X):
        total[i] += x

print("Yes" if all([a <= t for a, t in zip(A, total)]) else "No")
