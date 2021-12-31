t = input()
ans = []
for s in t:
    if s == '?':
        ans.append("D")
    else:
        ans.append(s)
print("".join(ans))