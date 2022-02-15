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



# S = input()

# red, blue = 0, 0
# for s in S:
#     if s == '0':
#         red += 1
#     else:
#         blue += 1

# print(min(red, blue) * 2)