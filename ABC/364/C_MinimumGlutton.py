def calc(A, limit):
    A.sort(reverse=True)
    total = 0
    for i, a in enumerate(A):
        total += a
        if total > limit:
            return i + 1
    return len(A)


N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(min(calc(A, X), calc(B, Y)))
