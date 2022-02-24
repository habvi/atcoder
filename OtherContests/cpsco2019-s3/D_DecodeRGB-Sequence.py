n = int(input())
s = input()

ans = True
for i in range(2):
    if i == 0:
        if s[0] != 'R':
            ans = False
        if s[-1] != 'B':
            ans = False
    else:
        if s[1] not in 'RG':
            ans = False
        if s[-2] not in 'GB':
            ans = False

print('Yes' if (ans and 'RGB' in s and 'GG' not in s and 'RB' not in s) else 'No')