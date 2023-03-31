def dist(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


R, C = map(int, input().split())
B = [list(input()) for _ in range(R)]

for i in range(R):
    for j in range(C):
        if B[i][j] in ".#":
            continue
        d = int(B[i][j])
        for ni in range(R):
            for nj in range(C):
                if B[ni][nj] == '#' and dist(i, j, ni, nj) <= d:
                    B[ni][nj] = '.'
        B[i][j] = '.'
for b in B:
    print(''.join(b))
