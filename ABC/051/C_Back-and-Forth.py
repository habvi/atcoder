sx, sy, gx, gy = map(int, input().split())

dy = gy - sy
dx = gx - sx

route = 'U'*dy + 'R'*dx + 'D'*dy + 'L'*dx \
        + 'L' + 'U'*(dy + 1) + 'R'*(dx + 1) + 'D' \
        + 'R' + 'D'*(dy + 1) + 'L'*(dx + 1) + 'U'
print(route)