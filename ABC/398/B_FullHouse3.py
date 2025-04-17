from itertools import combinations
from collections import Counter

A = list(map(int, input().split()))
for com in combinations(A, 5):
    c = Counter(com)
    if sorted(c.values()) == [2, 3]:
        print("Yes")
        exit()
print("No")
