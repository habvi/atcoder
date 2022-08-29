# hamamuさん解
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

INF = float('inf')
num = defaultdict(lambda : INF)
mx_a = []
new = 0
for a in A:
    if num[a] == INF:
        new += 1
        num[a] =  new
    mx_a.append(new)

mx = 0
mx_b = []
s = set()
kind_b = []
for b in B:
    nb = num[b]
    mx = max(mx, nb)
    mx_b.append(mx)
    s.add(nb)
    kind_b.append(len(s))

Q = int(input())
for _ in range(Q):
    x, y = map(lambda x: int(x) - 1, input().split())
    if mx_a[x] == mx_b[y] == kind_b[y]:
        print("Yes")
    else:
        print("No")