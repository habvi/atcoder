S = input()
od = 'RUD'
ev = 'LUD'
for i, s in enumerate(S):
    if i % 2 == 0:
        if s not in od:
            print('No')
            exit()
    else:
        if s not in ev:
            print('No')
            exit()
print('Yes')