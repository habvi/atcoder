from itertools import groupby

def ceil(x):
    return (x + 1) // 2

def floor(x):
    return x // 2


S = input()
ls = len(S)

lr = []
for k, v in groupby(S):
    lr.append((k, len(list(v))))

ans = [0] * ls
left, right = 0, 0
j = -1
for i, (_, num) in enumerate(lr):
    if i % 2 == 0:
        left += ceil(num)
        right += floor(num)
        j += num
    else:
        left += floor(num)
        right += ceil(num)
        ans[j] = left
        ans[j + 1] = right

        left, right = 0, 0
        j += num

print(*ans)