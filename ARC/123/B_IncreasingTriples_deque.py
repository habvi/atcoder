from collections import deque
n = int(input())
A = sorted(map(int, input().split()))
B = deque(sorted(map(int, input().split())))
C = deque(sorted(map(int, input().split())))
print(A)

ans = 0
for a in A:
    while B and B[0] <= a:
        B.popleft()
    if not B:
        print(ans) 
        exit()
        
    b = B.popleft()
    while C and C[0] <= b:
        C.popleft()
    if not C:
        print(ans)
        exit()
    ans += 1
    C.popleft()
    print(a, B, C)
    print('---')
print(ans)