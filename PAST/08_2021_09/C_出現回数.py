from collections import Counter

n, X = map(int, input().split())
A = list(map(int, input().split()))

c = Counter(A)
print(c[X])