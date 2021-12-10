n, x = map(int, input().split())
hum = [(0, 0, 1, 0, 0), (1, 1, 1, 1, 1)]
ac = [(0, 0, 1, 1, 1), (1, 2, 3, 4, 5)]
pts = [1, 3]
for i in range(n - 1):
    pts.append(pts[-1] * 2 + 1)
    sm = sum(hum[-1])
    hum.append((1, sm, 1, sm, 1))
    ac.append((1, sm + 1, sm + 2, 2*sm + 2, 2*sm + 3))

def solve(n, x):
    if n == 0:
        return pts[0]

    if x == ac[n][0]:
        return 0
    if x == ac[n][2]:
        return pts[n - 1] + 1
    if x == ac[n][4]:
        return pts[n]

    if x <= ac[n][1]:
        return solve(n - 1, x - 1)
    if x <= ac[n][3]:
        return pts[n - 1] + 1 + solve(n - 1, x - ac[n][2])
        
print(solve(n, x))