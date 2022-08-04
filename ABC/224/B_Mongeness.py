H, W = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(H)]

ans = 0
total = 0
for i1 in range(H):
    for i2 in range(i1 + 1, H):
        for j1 in range(W):
            for j2 in range(j1 + 1, W):
                total += 1
                ans += (A[i1][j1] + A[i2][j2] <= A[i2][j1] + A[i1][j2])
print("Yes" if ans == total else "No")