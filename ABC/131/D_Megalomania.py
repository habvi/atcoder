N = int(input())
ab = [tuple(map(int, input().split())) for _ in range(N)]

ab.sort(key=lambda x: x[1])
now = 0
for l, r in ab:
    now += l
    if now > r:
        print("No")
        exit()
print("Yes")