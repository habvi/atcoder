n = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
ans = A[0]
res = n - 2
for a in A[1:]:
    if not res:
        break
    num = min(2, res)
    ans += a * num
    res -= num
print(ans)