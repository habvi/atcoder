import sys
input = sys.stdin.readline
from math import sqrt

def add_(i):
    global now
    ai = A[i]
    now -= count_[ai] // 2
    count_[ai] += 1
    now += count_[ai] // 2

def delete(i):
    global now
    ai = A[i]
    now -= count_[ai] // 2
    count_[ai] -= 1
    now += count_[ai] // 2


n = int(input())
A = list(map(lambda x: int(x) - 1, input().split()))

Q = int(input())
qs = []
for i in range(Q):
    l, r = map(lambda x: int(x) - 1, input().split())
    qs.append((l, r, i))

# D = max(1, int(n // Q ** 0.5))
D = max(1, int(sqrt(3)*n // sqrt(Q)))

qs.sort(key=lambda x: (x[1] // D, x[0]))

ans = [0] * Q
nl, nr = 0, -1
now = 0
count_ = [0] * n
for l, r, i in qs:
    while nl < l:
        delete(nl)
        nl += 1
    while nl > l:
        nl -= 1
        add_(nl)
    while nr < r:
        nr += 1
        add_(nr)
    while nr > r:
        delete(nr)
        nr -= 1
    ans[i] = now

print(*ans)