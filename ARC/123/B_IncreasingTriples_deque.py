from collections import deque

n = int(input())
A = sorted(map(int, input().split()))
B = deque(sorted(map(int, input().split())))
C = deque(sorted(map(int, input().split())))

ans = 0
for a in A:
    while B and B[0] <= a:
        B.popleft()

    if not B:
        break
    b = B.popleft()

    while C and C[0] <= b:
        C.popleft()
    if not C:
        break
    C.popleft()

    ans += 1
print(ans)