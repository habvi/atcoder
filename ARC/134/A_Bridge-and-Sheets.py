n, l, w = map(int, input().split())
A = list(map(int, input().split()))

now = 0
ans = 0
for a in A:
    if a > now:
        must = (a - now + w - 1) // w
        ans += must
    now = a + w

ans += (l - now + w - 1) // w
print(ans)