A, B, C = map(int, input().split())

now = A
for _ in range(B):
    if now % B == C:
        print('YES')
        exit()
    now += A

print('NO')