from collections import deque

K = int(input())

que = deque(range(1, 10))

for _ in range(K - 1):
    x = que.popleft()
    t = x % 10
    if t - 1 >= 0:
        que.append(x * 10 + t - 1)
    que.append(x * 10 + t)
    if t + 1 <= 9:
        que.append(x * 10 + t + 1)

print(que.popleft())