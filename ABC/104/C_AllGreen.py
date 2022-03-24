def ceil(a, b):
    return (a + b - 1) // b


D, G = map(int, input().split())
pc = [tuple(map(int, input().split())) for _ in range(D)]

ans = float('inf')
for bit in range(1 << D):
    sum_p = 0
    sum_q = 0
    for i in range(D):
        if bit >> i & 1:
            q, bonus = pc[i]
            sum_p += q * (i + 1) * 100 + bonus
            sum_q += q

    if sum_p >= G:
        ans = min(ans, sum_q)
        continue

    for i in range(D):
        sum_np = sum_p
        sum_nq = sum_q
        if not bit >> i & 1:
            q, _ = pc[i]
            res = G - sum_np
            can = min(q - 1, ceil(res, (i + 1) * 100))
            sum_np += can * (i + 1) * 100
            sum_nq += can

            if sum_np >= G:
                ans = min(ans, sum_nq)
print(ans)