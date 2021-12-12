n = int(input())
A = list(map(int, input().split()))
g = 1
ans = [0] * (n + 1)
now = 0
for i, a in enumerate(A):
    if g and now > a:
        ans[i] = 1
        g = 0
    if not g and now < a:
        ans[i] = 1
        g = 1
    now = a

if not g:
    ans[-1] = 1
print(*ans[1:])