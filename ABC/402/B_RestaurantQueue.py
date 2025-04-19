from collections import deque

Q = int(input())

que = deque([])
for _ in range(Q):
    query = tuple(map(int, input().split()))
    if query[0] == 1:
        X = query[1]
        que.append(X)
    else:
        print(que.popleft())
