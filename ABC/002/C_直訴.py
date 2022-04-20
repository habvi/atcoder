def dist_two_points(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

def dist_line_to_point(x1, y1, x2, y2, px, py):
    nmrt = abs((y2 - y1)*px + (x1 - x2)*py + x2*y1 - y2*x1)
    dnmnt = ((y2 - y1)**2 + (x2 - x1)**2) ** 0.5
    return nmrt / dnmnt


ax, ay, bx, by, cx, cy = map(int, input().split())

print(dist_two_points(ax, ay, bx, by)
      * dist_line_to_point(ax, ay, bx, by, cx, cy) / 2)