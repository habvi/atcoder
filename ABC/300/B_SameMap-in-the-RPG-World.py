H, W = map(int, input().split())
A = [input() for _ in range(H)]
B = [input() for _ in range(H)]

for si in range(H):
    for sj in range(W):
        ok = True
        for i in range(H):
            for j in range(W):
                ni = (si + i) % H
                nj = (sj + j) % W
                if A[ni][nj] != B[i][j]:
                    ok = False
        if ok:
            print("Yes")
            exit()
print("No")
