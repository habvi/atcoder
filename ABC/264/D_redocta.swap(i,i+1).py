S = list(input())
W = "atcoder"

ans = 0
for w in W:
    i = S.index(w)
    ans += i
    S.pop(i)
print(ans)