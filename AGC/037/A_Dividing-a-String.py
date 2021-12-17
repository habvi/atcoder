s = input()
n = len(s)
cnt = 0
t = s[0]
i = 1
while i < n:
    if t == s[i]:
        if i == n - 1:
            break
        t = s[i:i+2]
        cnt += 1
        i += 2
    else:
        t = s[i]
        cnt += 1
        i += 1
print(cnt + 1)