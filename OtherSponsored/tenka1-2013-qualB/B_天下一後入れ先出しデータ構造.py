Q, L = map(int, input().split())

stack = []
total = 0
for _ in range(Q):
    *q, = input().split()
    if (q0 := q[0]) == 'Push':
        n, num = map(int, q[1:])
        if L - total < n:
            print('FULL')
            exit()
        stack.append([num, n])
        total += n

    elif q0 == 'Pop':
        n = int(q[1])
        while stack and n > 0:
            minus = min(stack[-1][1], n)
            stack[-1][1] -= minus
            n -= minus
            total -= minus
            if not stack[-1][1]:
                stack.pop()
        if n:
            print('EMPTY')
            exit()

    elif q0 == 'Top':
        if not stack:
            print('EMPTY')
            exit()
        print(stack[-1][0])

    else:
        print(total)

print('SAFE')