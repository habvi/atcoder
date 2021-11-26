s = input()
n = len(s)
ans = 0
for i in range(n):
    if i == 0 and s[i] == 'U':
        ans += n - 1
    elif i == n - 1 and s[i] == 'D':
        ans += n - 1
    else:
        if s[i] == 'D':
            ans += 2 * (n - i - 1) + i
        else:
            ans += n - i - 1 + 2 * i
print(ans)