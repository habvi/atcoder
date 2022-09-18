from collections import Counter

A = list(map(int, input().split()))

c = Counter(A)
print("Yes" if sorted(c.values()) == [2, 3] else "No")