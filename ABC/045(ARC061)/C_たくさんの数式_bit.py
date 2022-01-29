S = input()
n = len(S)

ans = 0
for bit in range(1 << n - 1):
    t = S[0]
    for i in range(n - 1):
        if bit >> i & 1:
            t += '+'
        t += S[i + 1]
    ans += eval(t)
print(ans)