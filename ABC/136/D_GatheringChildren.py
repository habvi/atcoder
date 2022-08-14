from itertools import groupby

def ceil(x):
    return (x + 1) // 2

def floor(x):
    return x // 2


S = input()
n = len(S)

i = 0
ans = [0] * n
for lr, v in groupby(S):
    num = len(list(v))
    if lr == 'L':
        ans[i - 1] += floor(num)
        ans[i] += ceil(num)
        i += num
    else:
        i += num
        ans[i - 1] += ceil(num)
        ans[i] += floor(num)
print(*ans)