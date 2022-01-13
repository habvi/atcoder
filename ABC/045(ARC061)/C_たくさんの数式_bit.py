s = input()
n = len(s)
ans = 0
for i in range(1 << n-1):
    tot = s[0]
    for j in range(n - 1):
        if i & (1<<j):
            tot += "+" + s[j + 1]
        else:
            tot += s[j + 1]
    ans += eval(tot)
print(ans)