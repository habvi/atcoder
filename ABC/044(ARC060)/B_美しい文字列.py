from collections import Counter

W = input()
print("Yes" if all(c % 2 == 0 for c in Counter(W).values()) else "No")