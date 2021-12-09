from itertools import product
n, k = map(int, input().split())
t = [tuple(map(int, input().split())) for _ in range(n)]
for pr in product((i for i in range(k)), repeat=n):
    xor = 0
    for i, p in enumerate(pr):
        xor ^= t[i][p]
    if xor == 0:
        print('Found')
        exit()
print('Nothing')