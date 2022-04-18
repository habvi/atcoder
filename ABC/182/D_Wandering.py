n = int(input())
A = list(map(int, input().split()))

mx = 0
total = 0
ans = -float('inf')
now = 0
for a in A:
    total += a
    mx = max(mx, total)
    ans = max(ans, now + mx)
    now += total
print(ans)