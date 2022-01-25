from itertools import combinations

h, w, a, b = map(int, input().split())

ans = 0
for com in combinations(range(h * w), a):
    for bit in range(1 << a):
        seen = 0
        ok = True
        # 0 : 縦, 1 : 横
        for i, k in enumerate(com):
            if seen >> k & 1:
                ok = False
                break
            seen |= 1 << k
            
            if bit >> i & 1 and (k + 1) % w != 0:
                nxt = k + 1
                if seen >> nxt & 1:
                    ok = False
                    break
                seen |= 1 << nxt
            elif bit >> i & 1 == 0 and k + w < h * w:
                nxt = k + w
                if seen >> nxt & 1:
                    ok = False
                    break
                seen |= 1 << nxt
            else:
                ok = False
                break
                
        if ok:
            ans += 1
    
print(ans)