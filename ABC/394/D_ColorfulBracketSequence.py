S = input()

stack = []
for s in S:
    if stack and stack[-1] + s in ("()", "[]", "<>"):
        stack.pop()
    else:
        stack.append(s)
print("Yes" if not stack else "No")
