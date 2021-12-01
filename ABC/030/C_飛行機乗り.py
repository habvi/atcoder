from bisect import bisect_left
n, m = map(int, input().split())
X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
t = 0
i = 0
cnt = 0
while t <= A[-1] or t <= B[-1]:
    bi = bisect_left(A, t)
    if bi >= n: break
    t = A[bi] + X
    if t > B[-1]:
        break
    cnt += 1

    bi = bisect_left(B, t)
    if bi >= m: break
    t = B[bi] + Y
    cnt += 1
print(cnt // 2)