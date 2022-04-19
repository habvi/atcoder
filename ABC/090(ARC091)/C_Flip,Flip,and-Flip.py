n, m = map(int, input().split())

if n == m == 1:
    print(1)
    exit()

if n == 1 or m == 1:
    minus = 2
else:
    minus = 2 * m + 2 * n - 4
print(n * m - minus)