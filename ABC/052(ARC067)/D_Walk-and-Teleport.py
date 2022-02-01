n, a, b = map(int, input().split())
X = list(map(int, input().split()))

ans = 0
for i in range(n - 1):
    walk = a * (X[i + 1] - X[i])
    ans += min(walk, b)
print(ans)