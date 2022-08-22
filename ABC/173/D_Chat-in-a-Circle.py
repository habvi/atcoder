N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
ans = A[0]
N -= 2
for a in A[1:]:
    ans += a * min(N, 2)
    N -= 2
    if N <= 0:
        break
print(ans)