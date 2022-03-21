S = input()
n = len(S)

ans = True
if (S[0] == 'A') and (S[2 : n - 1].count('C') == 1):
    for s in S:
        if s in 'AC':
            continue
        ans &= (s.islower())
else:
    ans = False

print('AC' if ans else 'WA')