n = int(input())
S = input()

stack = []
ans = n
for s in S:
    if s == 'x' and ''.join(stack[-2:]) == 'fo':
        stack.pop()
        stack.pop()
        ans -= 3
    else:
        stack.append(s)

print(ans)