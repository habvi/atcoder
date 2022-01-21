s = input()
t = input()
ls = len(s)
lt = len(t)

ans = float('inf')
for i in range(ls - lt + 1):
    cnt = 0
    for j in range(lt):
        if s[i + j] != t[j]:
            cnt += 1
    ans = min(ans, cnt)
print(ans)