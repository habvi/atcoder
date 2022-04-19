S = input()

pre = ''
now = ''
ans = 0
for s in S:
    now += s
    if pre != now:
        ans += 1
        pre = now
        now = ''
print(ans)