C = [list(map(int, input().split())) for _ in range(3)]

mn = []
for i in range(3):
    mn.append(min(C[i]))

for i in range(3):
    for j in range(3):
        C[i][j] -= mn[i]

print("Yes" if C[0] == C[1] == C[2] else "No")
