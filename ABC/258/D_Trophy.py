N, X = map(int, input().split())

total = 0
ans = float('inf')
for i in range(N):
    a, b = map(int, input().split())
    total += (a + b)
    X -= 1
    if X == 0:
        break
    ans = min(ans, total + b * X)
print(ans)