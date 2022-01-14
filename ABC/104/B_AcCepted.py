s = input()
if s[0] == 'A' and s[2 : len(s) - 1].count('C') == 1:
    for t in s:
        if t in 'AC':
            continue
        if not t.islower():
            print('WA')
            exit()
    print('AC')
else:
    print('WA')