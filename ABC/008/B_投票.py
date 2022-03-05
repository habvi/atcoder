from collections import Counter

n = int(input())

c = Counter([input() for _ in range(n)])
print(c.most_common()[0][0])