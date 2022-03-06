h, w, a, b = map(int, input().split())

ans = [['0'] * w for _ in range(h)]

for i in range(b):
    for j in range(a):
        ans[i][j] = '1'

for i in range(b, h):
    for j in range(a, w):
        ans[i][j] = '1'

for a in ans:
    print(''.join(a))