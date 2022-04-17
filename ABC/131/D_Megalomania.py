n = int(input())
ab = [tuple(map(int, input().split())) for _ in range(n)]

ab.sort(key=lambda x: x[1])

right = 0
for a, r in ab:
    if r - a < right:
        print('No')
        exit()
    right += a

print('Yes')