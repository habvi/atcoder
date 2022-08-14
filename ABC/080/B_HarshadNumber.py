def f(X):
    return sum(int(x) for x in str(X))


N = int(input())
print("Yes" if N % f(N) == 0 else "No")