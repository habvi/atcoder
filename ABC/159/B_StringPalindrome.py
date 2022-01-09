s = input()
n = len(s) // 2
if s == s[::-1] and s[:n] == s[-n:]:
    print('Yes')
else:
    print('No')