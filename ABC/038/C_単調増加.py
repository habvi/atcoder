from collections import deque

N = int(input())
A = list(map(int, input().split()))

d = deque()
ans = 0
for a in A:
    if d and d[-1] >= a:
        d = deque()
    d.append(a) 
    ans += len(d)
print(ans)