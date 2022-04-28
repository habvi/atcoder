def make753(s):
    global ans
    if s:
        if int(s) <= n:
            ans += (len(set(s)) == 3)
        else:
            return

    for t in '753':
        make753(s + t)


n = int(input())

ans = 0
make753('')
print(ans)