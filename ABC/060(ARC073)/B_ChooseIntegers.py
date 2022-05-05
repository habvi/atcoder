A, B, C = map(int, input().split())

for x in range(A, A * B + 1, A):
    if x % B == C:
        print('YES')
        exit()
print('NO')