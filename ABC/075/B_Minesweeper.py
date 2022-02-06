h, w = map(int, input().split())
S = [list(input()) for _ in range(h)]

for i in range(h):
    for j in range(w):
        if S[i][j] =='#':
            continue

        inc = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx == dy == 0:
                    continue
                ny, nx = i + dy, j + dx
                if not (0 <= ny < h and 0 <= nx < w):
                    continue
                if S[ny][nx] == '#':
                    inc += 1
        S[i][j] = str(inc)

for s in S:
    print(''.join(s))