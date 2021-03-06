from collections import deque

def fin():
    print('No')
    exit()


n = int(input())
A = list(map(int, input().split()))
q = deque(A)

k = 0
while q:
    if q[0] != k:
        fin()

    q.popleft()
    while q and q[-1] == k:
        q.pop()
    k = 1 - k

print('Yes')