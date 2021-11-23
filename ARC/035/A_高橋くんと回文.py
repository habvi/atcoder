s = input()
n = len(s)
for i in range(n // 2):
    if s[i] == s[n-i-1] or s[i] == '*' or s[n-i-1] == '*':
        continue
    print('NO')
    exit()
print('YES')