h, w = map(int, input().split())
if h % 3 == 0 or w % 3 == 0:
    print(0)
    exit()

ans = float('inf')
for y in range(1, h):
    s1 = y * w
    x = w // 2
    s2 = (h - y)*x
    s3 = (h - y)*(w - x)
    ss = (s1, s2, s3)
    ans = min(ans, max(ss) - min(ss))

for x in range(1, w):
    s1 = x * h
    y = h // 2
    s2 = (w - x)*y
    s3 = (w - x)*(h - y)
    ss = (s1, s2, s3)
    ans = min(ans, max(ss) - min(ss))

for y in range(1, h - 1):
    s1 = y * w
    y2 = (h - y) // 2
    s2 = y2 * w
    s3 = (h - y - y2) * w
    ss = (s1, s2, s3)
    ans = min(ans, max(ss) - min(ss))

for x in range(1, w - 1):
    s1 = x * h
    x2 = (w - x) // 2
    s2 = x2 * h
    s3 = (w - x - x2) * h
    ss = (s1, s2, s3)
    ans = min(ans, max(ss) - min(ss))
print(ans)