def is_inside(ax, ay, bx, by, cx, cy, dx, dy):
    ab_ad = (bx - ax) * (dy - ay) - (by - ay) * (dx - ax)
    bc_bd = (cx - bx) * (dy - by) - (cy - by) * (dx - bx)
    ca_cd = (ax - cx) * (dy - cy) - (ay - cy) * (dx - cx)
    plus = (ab_ad > 0) + (bc_bd > 0) + (ca_cd > 0)
    minus = (ab_ad < 0) + (bc_bd < 0) + (ca_cd < 0)
    # inside the triangle
    if plus == 3 or minus == 3:
        return True
    # on the triangle
    if ab_ad * bc_bd * ca_cd == 0:
        return False
    # outside the triangle
    return False

def is_concave(xy):
    for i in range(4):
        ax, ay = xy[i % 4]
        bx, by = xy[(i + 1) % 4]
        cx, cy = xy[(i + 2) % 4]
        dx, dy = xy[(i + 3) % 4]
        if is_inside(ax, ay, bx, by, cx, cy, dx, dy):
            return True
    return False


xy = [tuple(map(int, input().split())) for _ in range(4)]
print("Yes" if not is_concave(xy) else "No")