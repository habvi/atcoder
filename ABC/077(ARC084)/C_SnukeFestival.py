from bisect import bisect, bisect_left

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
C.sort()

ans = 0
for b in B:
    a = bisect_left(A, b)
    c = bisect(C, b)
    ans += a * (n - c)
print(ans)