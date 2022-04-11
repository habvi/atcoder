from collections import deque

Q = int(input())

que = deque([])
for _ in range(Q):
    q, *a, = map(int, input().split())
    if q == 1:
        x, c = a
        que.append((x, c))
    else:
        num = a[0]
        total = 0
        while num > 0:
            x, c = que.popleft()
            mn = min(c, num)
            total += x * mn
            num -= mn
            c -= mn
            if c != 0:
                que.appendleft((x, c))
                break
        print(total)