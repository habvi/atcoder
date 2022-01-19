from itertools import groupby
n, a, b, c, d = map(int, input().split())
a, b = a - 1, b - 1
s = input()

def check(s):
    for k, g in groupby(s):
        if k == '#':
            if len(list(g)) >= 2:
                return False
    return True

ans = True
if c < d:
    ans &= check(s[a : c])
    ans &= check(s[b : d])
else:
    ans &= check(s[a : c])
    jump = False
    for k, g in groupby(s[b - 1 : d + 1]):
        if k == '.':
            if len(list(g)) >= 3:
                jump = True
    ans &= jump
print('Yes' if ans else 'No')