def concentration(w, s):
    return s / (w + s) * 100


A, B, C, D, E, F = map(int, input().split())

water = [0] * (F + 1)
water[0] = 1
for ab in (A, B):
    for i in range(F + 1):
        nxt = i + ab * 100
        if nxt <= F:
            water[nxt] |= water[i]

ans = []
for w, ok in enumerate(water):
    if w == 0 or not ok:
        continue

    mx = min(w // 100 * E, F - w)
    sugar = 0
    for c in range(mx // C + 1):
        for d in range(mx // D + 1):
            total = C * c + D * d
            if total <= mx:
                sugar = max(sugar, total)

    ans.append((w + sugar, sugar, concentration(w, sugar)))

ans.sort(key=lambda x: -x[2])

print(*ans[0][:2])