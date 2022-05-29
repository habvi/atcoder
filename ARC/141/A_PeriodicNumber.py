def solve():
    s = input()
    n = int(s)
    m = len(s)

    cand = set()
    if n == 10 ** (m - 1):
        cand.add(int('9' * (m - 1)))

    for i in range(m - 1, 0, -1):
        if m % i:
            continue

        head = int(s[:i])
        ok = True
        for j in range(i, m, i):
            nxt = int(s[j : j + i])
            if head < nxt:
                break
            elif head > nxt:
                ok = False
                break

        if ok:
            cand.add(int(str(head) * (m // i)))
        else:
            if head == 10 ** (i - 1):
                cand.add(int('9' * (m - 1)))
            else:
                cand.add(int(str(head - 1) * (m // i)))
    print(max(cand))


T = int(input())
for _ in range(T):
    solve()