n, T = map(int, input().split())
A = [*map(int, input().split()), float('inf')]

ans = 0
now = 0
for a in A:
    # ans += min(a - now, T)
    if a < now + T:
        ans += a - now
    else:
        ans += T
    now = a

print(ans)