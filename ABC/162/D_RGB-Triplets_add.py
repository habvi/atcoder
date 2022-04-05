def idx(c):
    return RGB.index(c)


n = int(input())
S = input()

RGB = 'RGB'
left = [0] * 3
ans = 0
for mid in range(n):
    mc = S[mid]
    for r in range(mid + 1, n):
        rc = S[r]
        if mc == rc:
            continue

        lc = 3 - idx(mc) - idx(rc)
        ans += left[lc]

        l = mid - (r - mid)
        if l >= 0 and S[l] not in (mc, rc):
            ans -= 1

    left[idx(mc)] += 1

print(ans)