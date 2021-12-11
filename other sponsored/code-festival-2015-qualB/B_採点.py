from collections import Counter
n, m = map(int, input().split())
a = list(map(int, input().split()))
c = Counter(a)
print(c.most_common(1)[0][0] if c.most_common(1)[0][1] > n // 2 else '?')