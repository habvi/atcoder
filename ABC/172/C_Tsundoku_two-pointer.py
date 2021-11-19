n, m, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
r = 0
tot = 0
for i in range(m):
    if tot + B[i] <= k:
        tot += B[i]
        r += 1
    else:
        break

ans = r
for l in range(n):
    if A[l] > k:
        break
    tot += A[l]
    l += 1
    while tot > k and r-1 >= 0:
        tot -= B[r-1]
        r -= 1
    # print('---', l, r, tot, l+r, ans)
    if tot > k or r < 0:
        break
    ans = max(ans, l + r)
print(ans)