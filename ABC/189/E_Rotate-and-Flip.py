n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]

m = int(input())
# x, y, p
x, y = [1, 0, 0], [0, 1, 0]
xs, ys = [x[:]], [y[:]]
for _ in range(m):
    q, *p = map(int, input().split())
    if q == 1:
        x = [-i for i in x]
        x, y = y, x
    elif q == 2:
        y = [-i for i in y]
        x, y = y, x
    elif q == 3:
        x = [-i for i in x]
        x[2] += 2 * p[0]
    else:
        y = [-i for i in y]
        y[2] += 2 * p[0]

    xs.append(x[:])
    ys.append(y[:])

Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    b -= 1
    x, y = xy[b]
    x_x_mul, x_y_mul, x_p = xs[a]
    y_x_mul, y_y_mul, y_p = ys[a]
    print(x*x_x_mul + y*x_y_mul + x_p, x*y_x_mul + y*y_y_mul + y_p)