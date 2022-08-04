N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

i = B[0][0]
if ((i - 1) % 7 + M - 1) >= 7:
    print("No")
    exit()

A = []
for _ in range(N):
    A.append([i + j for j in range(M)])
    i += 7
print("Yes" if A == B else "No")