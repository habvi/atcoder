sx, sy = map(int, input().split())
n = int(input())
z = [tuple(map(int, input().split())) for _ in range(n)]

ans = float('inf')
for i in range(n):
    (x1, y1), (x2, y2) = z[i], z[(i+1)%n]
    if x1 == x2:
        a = 1
        b = 0
        c = -x1
    else:
        a = (y2-y1) / (x2-x1)
        b = -1
        c = ((y2-y1) / (x2-x1)) * (-x1) + y1
    
    d = abs(a*sx + b*sy + c) / ((a**2 + b**2)**0.5)
    ans = min(ans, d)
print(ans)