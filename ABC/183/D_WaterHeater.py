from itertools import accumulate
n, w = map(int, input().split())
a = [0] * (2*10**5 + 5)
for _ in range(n):
    s, t, p = map(int, input().split())
    a[s] += p
    a[t] -= p

ac = list(accumulate(a))
print('Yes' if max(ac) <= w else 'No')