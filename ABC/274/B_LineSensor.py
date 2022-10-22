H, W = map(int, input().split())
C = [input() for _ in range(H)]

for c in zip(*C):
    print(c, c.count('#'))