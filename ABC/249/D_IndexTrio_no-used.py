from collections import Counter

def div_lis(x):
    div_l, div_r = [], []
    for i in range(1, int(x**0.5) + 1):
        if x % i != 0:
            continue
        div_l.append(i)
        if i != x // i:
            div_r.append(x // i)
    div = div_l + div_r[::-1]
    return div


n = int(input())
A = list(map(int, input().split()))

c = Counter(A)

ans = 0
for k, v in c.items():
    for x in div_lis(k):
        ans += v * c[x] * c[k // x]
print(ans)