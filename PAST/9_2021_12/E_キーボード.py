S = input()

left = range(1, 6)

ans = 0
for i, s in enumerate(S):
    if i == 0:
        ans += 500
        continue

    if s == (pre := S[i - 1]):
        ans += 301
    else:
        if (int(s) in left) == (int(pre) in left):
            ans += 210
        else:
            ans += 100
print(ans)