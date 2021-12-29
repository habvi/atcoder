n, p = map(int, input().split())
A = list(map(int, input().split()))
ev, od = 0, 0
for a in A:
    if a % 2 == 0:
        ev += 1
    else:
        od += 1

C = [[0]*(n+1) for _ in range(n+1)]
C[0][0] = 1
for i in range(n):
    for j in range(i+1):
        C[i+1][j] += C[i][j]
        C[i+1][j+1] += C[i][j]

cnt = 0
if od:
    for i in range(1, od + 1, 2):
        cnt += C[od][i]

if p == 0:
    ans = pow(2, n) - pow(2, ev) * cnt
else:
    ans = pow(2, ev) * cnt
print(ans)