s = input()
if len(s) % 2:
    if s[0] != s[-1]:
        print('First')
    else:
        print('Second')
else:
    if s[0] == s[-1]:
        print('First')
    else:
        print('Second')