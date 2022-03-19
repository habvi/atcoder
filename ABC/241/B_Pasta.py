from collections import Counter

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

c = Counter(A)
for b in B:
    if c[b] == 0:
        print('No')
        exit()
    c[b] -= 1

print('Yes')