n, x, y = map(int, input().split())
x, y = x - 1, y - 1

d = [0] * (n - 1)
for i in range(n):
    for j in range(i + 1, n):
        d[min(j - i, abs(i - x) + 1 + abs(y - j)) - 1] += 1
print(*d)