n, a, b = map(int, input().split())
if n <= 5:
    print(n * b)
else:
    tot = b * 5
    n -= 5
    tot += a * n
    print(tot)