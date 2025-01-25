H, W = map(int, input().split())
S = [input() for _ in range(H)]

INF = float("inf")
# xmin, xmax, ymin, ymax
edges = [INF, 0, INF, 0]
for i in range(H):
    for j in range(W):
        if S[i][j] != "#":
            continue
        edges[0] = min(edges[0], j)
        edges[1] = max(edges[1], j)
        edges[2] = min(edges[2], i)
        edges[3] = max(edges[3], i)

for i in range(edges[2], edges[3] + 1):
    for j in range(edges[0], edges[1] + 1):
        if S[i][j] == ".":
            print("No")
            exit()
print("Yes")
