n = int(input())
A = list(map(int, input().split()))
d = {a : i for i, a in enumerate(A, 1)}
print(*[d[i] for i in range(1, n + 1)])