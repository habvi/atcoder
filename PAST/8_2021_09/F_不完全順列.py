n = int(input())
S = input()

ans = [None] * n
idx = []
num = []
for i, s in enumerate(S):
    if s == '1':
        ans[i] = i + 1
    else:
        idx.append(i)
        num.append(i + 1)

if len(idx) == 1:
    print(-1)
    exit()

if not num:
    print(*ans)
    exit()

num.append(num.pop(0))
for i, x in zip(idx, num):
    ans[i] = x
print(*ans)