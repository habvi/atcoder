N = int(input())

A = []
for i in range(N):
    B = []
    for j in range(i + 1):
        if j in (0, i):
            B.append(1)
        else:
            B.append(A[j - 1] + A[j])
    A = B
    print(*A)
