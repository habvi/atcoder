S = input()

stack = []
ans = 0
for s in S:
    if stack and stack[-1] != s:
        stack.pop()
        ans += 2
    else:
        stack.append(s)

print(ans)