N = int(input())
A = list(map(int, input().split()))
Q = int(input())
for _ in range(Q):
    q, *X = map(int, input().split())
    if q == 1:
        k, x = X
        A[k - 1] = x
    else:
        k = X[0]
        print(A[k - 1])