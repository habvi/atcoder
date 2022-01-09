s = input()
n = len(s) // 2
for i in range(n):
    if s[i] != s[~i]:
        print('No')
        exit()
print('Yes' if s[:n] == s[-n:] else 'No')