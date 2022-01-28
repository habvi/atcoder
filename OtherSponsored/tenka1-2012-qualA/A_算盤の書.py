from collections import deque

n = int(input())

d = deque([0, 1], maxlen=2)
for _ in range(n):
    d.append(sum(d))
print(d[-1])