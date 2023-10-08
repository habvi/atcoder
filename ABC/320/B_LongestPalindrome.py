S = input()

n = len(S)
ans = 0
for i in range(n):
    for j in range(i + 1, n + 1):
        s = S[i : j]
        if s == s[::-1]:
            ans = max(ans, len(s))
print(ans)