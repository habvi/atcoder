S = input()
n = len(S)

if len(set(S)) != n or S == S.lower() or S == S.upper():
    print('No')
else:
    print('Yes')