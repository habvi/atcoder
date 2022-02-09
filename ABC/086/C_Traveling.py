n = int(input())
P = [tuple(map(int, input().split())) for _ in range(n)]
P = [(0, 0, 0), *P]

for i in range(n):
    t1, x1, y1 = P[i]
    t2, x2, y2 = P[i + 1]
    dst = abs(x1 - x2) + abs(y1 - y2)
    t = t2 - t1

    if dst > t or dst % 2 != t % 2:
        print('No')
        exit()
print('Yes')