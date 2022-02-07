from collections import deque

n = int(input())
A = list(map(int, input().split()))

qx = deque()
qs = deque()
ans = 0
xor, sigma = 0, 0
for x, s in zip(A, A):
    qx.append(x)
    qs.append(s)
    xor ^= x
    sigma += s

    while qx and xor != sigma:
        xor ^= qx.popleft()
        sigma -= qs.popleft()

    ans += len(qx)
print(ans)