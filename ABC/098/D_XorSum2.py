from collections import deque

n = int(input())
A = list(map(int, input().split()))

qx = deque()
qs = deque()
ans = 0
xor, sigma = 0, 0
for a in A:
    qx.append(a)
    qs.append(a)
    xor ^= a
    sigma += a

    while qx and xor != sigma:
        xor ^= qx.popleft()
        sigma -= qs.popleft()

    ans += len(qx)
print(ans)