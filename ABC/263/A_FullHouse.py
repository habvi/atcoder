from collections import Counter

A = list(map(int, input().split()))

c = Counter(A)
values = list(c.values())
print("Yes" if sorted(values) == [2, 3] else "No")