n = int(input())
x = list(map(int, input().split()))
sx = sorted(x)
r = sx[n // 2]
l = sx[n // 2 - 1]

for a in x:
    if a < r:
        print(r)
    else:
        print(l)