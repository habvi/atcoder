n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]

ab.sort(key=lambda x: -sum(x))

T, A = 0, 0
for i, (a, b) in enumerate(ab):
    if i % 2:
        A += b
    else:
        T += a
print(T - A)