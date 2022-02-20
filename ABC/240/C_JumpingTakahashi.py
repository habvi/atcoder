n, x = map(int, input().split())

reach = set()
reach.add(0)
for _ in range(n):
    a, b = map(int, input().split())
    next_ = set()
    for m in reach:
        next_.add(m + a)
        next_.add(m + b)
    reach = next_

print('Yes' if x in reach else 'No')