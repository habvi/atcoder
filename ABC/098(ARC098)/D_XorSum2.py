from collections import deque

n = int(input())
A = list(map(int, input().split()))

q = deque()
xor, sigma = 0, 0
ans = 0
for a in A:
    q.append(a)
    xor ^= a
    sigma += a

    while q and xor != sigma:
        rm = q.popleft()
        xor ^= rm
        sigma -= rm

    ans += len(q)
print(ans)