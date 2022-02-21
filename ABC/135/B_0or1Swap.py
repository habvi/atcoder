def is_ordered(A):
    for i in range(n - 1):
        if A[i + 1] - A[i] < 0:
            return False
    return True


n = int(input())
P = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        P[i], P[j] = P[j], P[i]
        if is_ordered(P):
            print('YES')
            exit()
        P[i], P[j] = P[j], P[i]

print('NO')