from collections import Counter

def comb(n):
    return n * (n - 1) // 2


n, m = map(int, input().split())
A = list(map(int, input().split()))

ac = [A[0] % m]
for a in A[1:]:
    ac.append((ac[-1] + a) % m) 

c = Counter(ac)

ans = c[0]
for k, v in c.items():
    if v >= 2:
        ans += comb(v)
print(ans)