a, n = map(int, input().split())
ln = len(str(n))

pre = set([1])
used = set()
ans = 0
while pre:
    nxt = set()
    for p in pre:
        if p == n:
            print(ans)
            exit()
            
        used.add(p)
        if p >= 10 and p % 10:
            s = str(p)
            ss = int(s[-1] + s[:-1])
            if len(str(ss)) <= ln and ss not in used:
                nxt.add(ss)
        pa = p * a
        if len(str(pa)) <= ln and pa not in used:
            nxt.add(pa)
    pre = nxt
    ans += 1   
print(-1)