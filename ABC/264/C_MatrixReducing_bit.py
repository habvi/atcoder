H, W = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(H)]
H2, W2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H2)]

for h in range(1, 1 << H):
    for w in range(1, 1 << W):
        ct = 0
        k = 0
        for i in range(H):
            if not h >> i & 1:
                continue
            if k >= H2:
                break
            l = 0
            for j in range(W):
                if not w >> j & 1:
                    continue
                if l >= W2:
                    break
                ct += (A[i][j] == B[k][l])
                l += 1
            k += 1
        if ct == H2 * W2:
            print("Yes")
            exit()
print("No")