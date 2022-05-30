# hamamuさん解
from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

INF = float('inf')
num = defaultdict(lambda : INF)
a_mx = [0] * n
x = 1
for i, a in enumerate(A):
    if num[a] == INF:
        num[a] =  x
        a_mx[i] = x
        x += 1
    else:
        a_mx[i] = a_mx[i - 1]

mx = 0
b_kind = [None] * n
s = set()
b_mx = [0] * n
for i, b in enumerate(B):
    s.add(num[b])
    b_kind[i] = len(s)
    mx = max(mx, num[b])
    b_mx[i] = mx

Q = int(input())
for _ in range(Q):
    x, y = map(lambda x: int(x) - 1, input().split())
    print("Yes" if a_mx[x] == b_kind[y] == b_mx[y] else "No")