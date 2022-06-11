n = int(input())
K = int(input())
for _ in range(K):
    a, b = map(int, input().split())

    col = min(a - 1, n - a)
    row = min(b - 1, n - b)
    print(min(row, col) % 3 + 1)