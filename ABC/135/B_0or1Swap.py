n = int(input())
P = list(map(int, input().split()))

correct = list(range(1, n + 1))

for i in range(n):
    for j in range(i, n):
        P[i], P[j] = P[j], P[i]
        if P == correct:
            print('YES')
            exit()

        P[i], P[j] = P[j], P[i]
print('NO')