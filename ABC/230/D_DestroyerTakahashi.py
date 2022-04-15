n, D = map(int, input().split())
lr = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(n)]

lr.sort(key=lambda x: x[1])

ans = 0
right = -1
for l, r in lr:
    if l <= right:
        continue
    ans += 1
    right = r + D - 1
print(ans)