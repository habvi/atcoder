total, m, a, b = map(int, input().split())

for i in range(m):
    c = int(input())
    if total <= a:
        total += b

    total -= c
    if total < 0:
        print(i + 1)
        exit()

print('complete')