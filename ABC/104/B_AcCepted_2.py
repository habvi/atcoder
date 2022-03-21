S = input()
n = len(S)

ans = True
c = 0
for i, s in enumerate(S):
    if i == 0:
        ans &= (s == 'A')
    elif 2 <= i < n - 1 and s == 'C':
        c += 1
    else:
        ans &= (s.islower())

ans &= (c == 1)
print('AC' if ans else 'WA')