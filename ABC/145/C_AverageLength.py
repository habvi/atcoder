from itertools import permutations

def dist(x, y, x2, y2):
    return ((x - x2)**2 + (y - y2)**2) ** 0.5


n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]

total = 0
num = 0
for p in permutations(xy):
    num += 1
    for i in range(n - 1):
        (x1, y1), (x2, y2) = p[i], p[i + 1]
        total += dist(x1, y1, x2, y2)

print(total / num)