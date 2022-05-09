h, w, K = map(int, input().split())
S = [input() for _ in range(h)]

ans = float('inf')
for bit in range(1 << h - 1):
    num_r = bin(bit).count('1') + 1
    row = [0] * num_r

    idx = [None] * h
    r = 0
    for i in range(h - 1):
        idx[i] = r
        if bit >> i & 1:
            r += 1
    idx[i + 1] = r

    total = num_r - 1
    ok = True
    for col in zip(*S):
        one = [0] * num_r
        for i, c in enumerate(col):
            if int(c):
                row[idx[i]] += 1
                one[idx[i]] += 1

        if any(x > K for x in one):
            ok = False
            break

        over = any(r > K for r in row)
        if over:
            total += 1
            row = one[:]

    if ok:
        ans = min(ans, total)
print(ans)