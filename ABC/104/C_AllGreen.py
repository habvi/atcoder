D, G = map(int, input().split())
S = [tuple(map(int, input().split())) + ((i + 1)*100,) for i in range(D)]
ans = float('inf')
for i in range(1 << D):
    tot_sc, tot_q = 0, 0
    for j in range(D):
        if i & (1<<j):
            n, bns, sc = S[j]
            tot_sc += sc*n + bns
            tot_q += n
    if tot_sc >= G:
        ans = min(ans, tot_q)

    for j in range(D):
        tot_sc2, tot_q2 = tot_sc, tot_q
        if i & (1<<j):
            n, bns, sc = S[j]
            if tot_sc2 < G:
                continue

            tot_sc2 -= bns + sc
            tot_q2 -= 1
            n -= 1
            if tot_sc2 < G:
                continue

            tot_q2 -= min(n, (tot_sc2 - G) // sc)
            ans = min(ans, tot_q2)
print(ans)