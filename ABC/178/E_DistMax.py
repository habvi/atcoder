n = int(input())
a, b = [], []
for _ in range(n):
    x, y = map(int, input().split())
    a.append(x - y)
    b.append(x + y)
print(max(max(a) - min(a), max(b) - min(b)))