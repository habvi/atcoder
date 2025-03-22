S = input()

ans = 0
i = 0
for s in S:
    if i % 2:
        if s == 'i':
            ans += 1
            i += 1
    else:
        if s == 'o':
            ans += 1
            i += 1
    i += 1
if i % 2:
    ans += 1
print(ans)
