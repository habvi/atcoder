a, r, n = map(int, input().split())

if r == 1:
    print(a)
    exit()

num = a
for _ in range(n - 1):
    num *= r
    if num > 10 ** 9:
        print('large')
        exit()

print(num)