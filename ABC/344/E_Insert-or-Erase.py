from collections import defaultdict

INF = float('inf')

N = int(input())
A = [0] + list(map(int, input().split())) + [INF]

left = defaultdict(int)
right = defaultdict(int)
m = len(A)
for i, a in enumerate(A):
    if i == 0:
        left[a] = -1
        right[a] = A[i + 1]
    elif i == m - 1:
        left[a] = A[i - 1]
        right[a] = -1
    else:
        left[a] = A[i - 1]
        right[a] = A[i + 1]

Q = int(input())
for _ in range(Q):
    q = input().split()
    qi = int(q[0])
    if qi == 1:
        l, x = int(q[1]), int(q[2])
        r = right[l]
        right[l] = x
        left[r] = x
        left[x] = l
        right[x] = r
    else:
        x = int(q[1])
        l = left[x]
        r = right[x]
        right[l] = r
        left[r] = l
        del left[x]
        del right[x]

x = right[0]
while x != INF:
    print(x)
    x = right[x]
