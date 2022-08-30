def is_counterclockwise(ax, ay, ox, oy, bx, by):
    cross_product = (ax - ox) * (by - oy) - (ay - oy) * (bx - ox)
    # counterclockwise
    if cross_product > 0:
        return True
    # straight line
    if cross_product == 0:
        return False
    # clockwise
    return False


xy = [tuple(map(int, input().split())) for _ in range(4)]

for i in range(4):
    ax, ay = xy[i % 4]
    ox, oy = xy[(i - 1) % 4]
    bx, by = xy[(i - 2) % 4]
    if not is_counterclockwise(ax, ay, ox, oy, bx, by):
        print("No")
        exit()
print("Yes")