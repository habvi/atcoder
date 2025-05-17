from collections import defaultdict

H, W, N = map(int, input().split())
trash_x = defaultdict(lambda: set())
trash_y = defaultdict(lambda: set())
for _ in range(N):
    X, Y = map(int, input().split())
    trash_x[X].add(Y)
    trash_y[Y].add(X)

Q = int(input())
for _ in range(Q):
    q, a = map(int, input().split())
    if q == 1:
        x = a
        print(len(trash_x[x]))
        for y in trash_x[x]:
            trash_y[y].remove(x)
        del trash_x[x]
    else:
        y = a
        print(len(trash_y[y]))
        for x in trash_y[y]:
            trash_x[x].remove(y)
        del trash_y[y]
