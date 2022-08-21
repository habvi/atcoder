X, Y, N = map(int, input().split())

div, mod = divmod(N, 3)
ans = min(X * N, Y * div + X * mod)
print(ans)