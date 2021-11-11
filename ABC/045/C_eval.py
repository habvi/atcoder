from itertools import product
s = input()
n = len(s)
ans = 0
for pr in product((0, 1), repeat=n-1):
    ev = ""
    for i in range(n-1):
        ev += s[i]
        ev += '+' if pr[i] else ''
    ev += s[-1]
    ans += eval(ev)
print(ans)