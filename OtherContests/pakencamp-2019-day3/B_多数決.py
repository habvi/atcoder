from collections import Counter

n = int(input())
A = [input() for _ in range(n)]

B = 'black'
W = 'white'

c = Counter(A)
count_b = c[B]
count_w = c[W]

print(B if count_b > count_w else W)