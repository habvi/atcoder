n = int(input())
A = list(map(int, input().split()))

stack = []
ans = 0
for a in A:
    if not stack or stack[-1][0] != a:
        stack.append([a, 1])
        ans += 1
    else:
        if stack[-1][1] + 1 == a:
            stack.pop()
            ans -= a - 1
        else:
            stack[-1][1] += 1
            ans += 1

    print(ans)