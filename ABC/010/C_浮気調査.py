xa, ya, xb, yb, T, V = map(int, input().split())
n = int(input())
d = T * V
cnt = 0
for _ in range(n):
    x, y = map(int, input().split())
    if ((x - xa)**2 + (y - ya)**2)**0.5 + ((xb - x)**2 + (yb - y)**2)**0.5 <= d:
        cnt += 1
print('YES' if cnt >= 1 else 'NO')