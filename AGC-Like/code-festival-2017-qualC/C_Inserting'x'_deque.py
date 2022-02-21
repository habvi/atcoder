from collections import deque

S = input()

T = [s for s in S if s != 'x']
if T != T[::-1]:
    print(-1)
    exit()

q = deque(S)

ans = 0
while len(q) >= 2:
    if q[0] == q[-1]:
        q.popleft()
        q.pop()
    else:
        if q[0] == 'x':
            q.popleft()
        else:
            q.pop()
        ans += 1

print(ans)