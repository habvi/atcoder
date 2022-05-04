n = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

ans = 0
for i, a in enumerate(A):
    ans += a * (n - i - 1)
    ans -= a * i
print(ans)