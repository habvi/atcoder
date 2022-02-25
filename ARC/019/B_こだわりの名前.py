S = input()
ls = len(S)

count_ = 0
for i in range(ls // 2):
    if S[i] != S[~i]:
        count_ += 1

ans = 0
for i in range(ls):
    if S[i] == S[~i]:
        ans += 25
    else:
        if count_ == 1:
            ans += 24
        else:
            ans += 25

if ls % 2 and count_ == 0:
    ans -= 25

print(ans)