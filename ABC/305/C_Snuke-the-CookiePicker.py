H, W = map(int, input().split())
S = [input() for _ in range(H)]

h_min, h_max = H, 0
w_min, w_max = W, 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            continue
        h_min = min(h_min, i)
        h_max = max(h_max, i)
        w_min = min(w_min, j)
        w_max = max(w_max, j)

for i in range(h_min, h_max + 1):
    for j in range(w_min, w_max + 1):
        if S[i][j] == '.':
            print(i + 1, j + 1)
            exit()