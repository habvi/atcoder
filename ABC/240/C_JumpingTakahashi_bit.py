n, x = map(int, input().split())

reach = 1
for _ in range(n):
    a, b = map(int, input().split())
    reach = reach << a | reach << b

print('Yes' if 1 << x & reach else 'No')