n, x = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

ans = 0
for i, a in enumerate(A):
    if i == n - 1:
        if a == x:
            ans += 1
        break
    
    if a <= x:
        ans += 1
        x -= a
    else:
        break

print(ans)