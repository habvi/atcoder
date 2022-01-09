n, m = map(int, input().split())
cnt = [1] * n
red = [0] * n
red[0] = 1
for _ in range(m):
    x, y = map(lambda x: int(x) - 1, input().split())
    cnt[x] -= 1
    cnt[y] += 1
    if red[x]:
        red[y] = 1
    if not cnt[x]:
        red[x] = 0
print(sum(red))