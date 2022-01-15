a, n = map(int, input().split())
ln = len(str(n))
pre = set([1])
ans = 0
used = set([1])
while True:
    nxt = set()
    for p in pre:
        used.add(p)
        if p == n:
            print(ans)
            exit()
        if p >= 10 and p % 10:
            s = str(p)
            ss = s[-1] + s[:-1]
            if len(ss) <= ln and int(ss) not in used:
                nxt.add(int(ss))
        if len(str(p * a)) <= ln and p * a not in used:
            nxt.add(p * a)
    pre = nxt
    ans += 1
    if not nxt:
        break    
print(-1)