# https://atcoder.jp/contests/tenka1-2017/tasks/tenka1_2017_d

def sum_val(x):
    total = 0
    for a, b in ab:
        la = a.bit_length()
        ok = True
        for i in range(la):
            if a >> i & 1 and x >> i & 1 == 0:
                ok = False
                break
        if ok:
            total += b
    return total


n, k = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]

lk = k.bit_length()

ans = sum_val(k)
for i in range(lk):
    if k >> i & 1:
        nk = k - (1 << i)
        nk |= (1 << i) - 1
        ans = max(ans, sum_val(nk))

print(ans)