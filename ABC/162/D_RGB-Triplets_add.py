def idx(c):
    return RGB.index(c)


N = int(input())
S = input()

RGB = "RGB"
ct = [0] * 3
ans = 0
for m in range(N):
    for r in range(m + 1, N):
        mid = S[m]
        right = S[r]
        if mid == right:
            continue
        i = 3 - idx(mid) - idx(right)
        ans += ct[i]
        l = m - (r - m)
        if 0 <= l and S[l] == RGB[i]:
            ans -= 1
    ct[idx(mid)] += 1
print(ans)