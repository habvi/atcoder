S = input()
c = input()

ans = ""
for s in S:
    if s == c:
        ans += c * 2
    else:
        ans += s
print(ans)