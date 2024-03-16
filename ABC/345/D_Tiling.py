from itertools import product, permutations

def put(tile, y, x, h, w):
    if y + h > H or x + w > W:
        return False
    for i in range(h):
        for j in range(w):
            if tile[y + i][x + j]:
                return False
            tile[y + i][x + j] = 1
    return True

def is_ok(per):
    tile = [[0] * W for _ in range(H)]
    idx = 0
    for i in range(H):
        for j in range(W):
            if not tile[i][j]:
                if idx == len(per):
                    return False
                if not put(tile, i, j, per[idx][0], per[idx][1]):
                    return False
                idx += 1
    return idx == len(per)


N, H, W = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(N)]

# 0:not use, 1:a,b , 2:b,a
for use in product((0, 1, 2), repeat=N):
    tiles = []
    for i, u in enumerate(use):
        a, b = ab[i]
        if u == 1:
            tiles.append((a, b))
        elif u == 2:
            tiles.append((b, a))
    for per in permutations(tiles):
        if is_ok(per):
            print("Yes")
            exit()
print("No")
