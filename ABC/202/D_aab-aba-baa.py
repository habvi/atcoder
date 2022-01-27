N = 60
C = [[0] * (N + 1) for _ in range(N + 1)]
C[0][0] = 1
for i in range(N):
    for j in range(i + 1):
        C[i + 1][j] += C[i][j]
        C[i + 1][j + 1] += C[i][j]

a, b, k = map(int, input().split())
ans = []
for _ in range(a + b):
    if a > 0:
        c = C[a + b - 1][a - 1]
    else:
        c = 0
    
    if k <= c:
        ans.append('a')
        a -= 1
    else:
        ans.append('b')
        b -= 1
        k -= c
print(''.join(ans))