x = input()
S = input()
ans = ""
for s in S:
    if s == x:
        continue
    ans += s
print(ans)