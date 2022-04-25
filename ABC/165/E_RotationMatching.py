def ceil(a, b):
    return (a + b - 1) // b


n, m = map(int, input().split())

mid = ceil(m, 2)
for i in range(mid):
    print(mid - i, mid + i + 1)

for i in range(m - mid):
    st = mid * 2 + (m - mid) + 1
    print(st - i - 1, st + i + 1)