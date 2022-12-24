from itertools import groupby

def ceil(a, b):
    return (a + b - 1) // b


S = input()

ans = 0
for k, v in groupby(S):
    v = len(list(v))
    if k == '0':
        ans += ceil(v, 2)
    else:
        ans += v
print(ans)