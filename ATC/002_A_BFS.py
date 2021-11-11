from collections import deque
def bfs(sy, sx, gy, gx):
    que = deque([])
    que.append((sy, sx))
    dist[sy][sx] = 0
    while que:
        y, x = que.popleft()
        for dx, dy in zip([0, 1, 0, -1], [1, 0, -1, 0]):
            ny = y+dy
            nx = x+dx
            if not (0 <= ny < r and 0 <= nx < c): continue
            if G[ny][nx] == '#': continue
            if dist[ny][nx] != -1: continue
            dist[ny][nx] = dist[y][x] + 1
            if ny == gy and nx == gx:
                print(dist[ny][nx])
                exit()
            que.append((ny, nx))

r, c = map(int, input().split())
sy, sx = map(lambda x: int(x)-1, input().split())
gy, gx = map(lambda x: int(x)-1, input().split())
G = [input() for _ in range(r)]
dist = [[-1]*c for _ in range(r)]
bfs(sy, sx, gy, gx)

'''
7 8
2 2
4 5
########
#......#
#.######
#..#...#
#..##..#
##.....#
########
'''