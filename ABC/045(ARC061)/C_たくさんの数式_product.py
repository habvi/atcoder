from itertools import product
s = input()
n = len(s)
ans = 0
for pr in product((0, 1), repeat=n-1):
    t = ""
    for i in range(n - 1):
        t += s[i]
        t += '+' if pr[i] else ''
    t += s[-1]
    ans += eval(t)
print(ans)