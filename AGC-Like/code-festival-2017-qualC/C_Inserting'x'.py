s = input()

n = len(s)
if len(set(s)) == 1:
    print(0)
    exit()

cnt = 0
i = 0
l = i
r = n - i - 1
while l < n and r > 0:
    if s[l] != s[r]:
        cnt += 1
        if s[l] == 'x':
            l += 1
        elif s[r] == 'x':
            r -= 1
        else:
            print(-1)
            exit()
    else:
        l += 1
        r -= 1
    if l >= r:
        break
print(cnt)