X, K, D = map(int, input().split())
X = abs(X)

if (d := K * D) <= X:
    print(X - d)
    exit()

div, m = divmod(X, D)
if (K - div) % 2 == 0:
    print(m)
else:
    print(abs(m - D))