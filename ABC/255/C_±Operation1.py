X, A, D, n = map(int, input().split())

if D == 0:
    print(abs(X - A))
    exit()

a = [A, A + D * (n - 1)]
a.sort()
mn, mx = a

if X <= mn:
    print(mn - X)
elif mx <= X:
    print(X - mx)
else:
    D = abs(D)
    mod = (X - A) % D
    print(min(mod, D - mod))