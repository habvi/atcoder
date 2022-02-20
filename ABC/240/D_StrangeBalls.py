n = int(input())
A = list(map(int, input().split()))

stack = [(-1, -1)]

for a in A:
    num, count_ = stack[-1]
    if num != a:
        stack.append((a, 1))
    else:
        if count_ + 1 == a:
            for _ in range(count_):
                stack.pop()
        else:
            stack.append((a, count_ + 1))

    print(len(stack) - 1)