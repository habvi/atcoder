from itertools import permutations

def dist(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5


n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]

ans = 0
num = 0
for per in permutations(range(n)):
    total = 0
    for i in range(n - 1):
        x1, y1 = xy[per[i]]
        x2, y2 = xy[per[i + 1]]
        total += dist(x1, y1, x2, y2)
    ans += total
    num += 1

print(ans / num)