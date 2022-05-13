from collections import Counter

def sigma_al(a, l):
    return ((a + l) * (l - a + 1)) // 2


n, K = map(int, input().split())
A = list(map(int, input().split()))

c = Counter(A)
B = [[0, 0]]
B.extend([[k, c[k]] for k in sorted(c.keys())])

ans = 0
while K:
    now, v = B.pop()
    if not B:
        break

    pre = B[-1][0]
    diff = now - pre
    if K <= diff * v:
        div, mod = divmod(K, v)
        ans += sigma_al(now - div + 1, now) * v
        ans += (now - div) * mod
        break

    ans += sigma_al(now - diff + 1, now) * v
    K -= diff * v
    B[-1][1] += v

print(ans)