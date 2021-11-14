n = int(input())
ans = 0
S = 10**11
for a in range(1, int(S**(1/3)) + 5):
    for b in range(a, int((S/a)**0.5) + 5):
        c = n // (a*b)
        if c < b: continue
        ans += (c - b + 1)
print(ans)