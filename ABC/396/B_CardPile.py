Q = int(input())
stack = [0] * 100
for _ in range(Q):
    q, *arg = map(int, input().split())
    if q == 1:
        x = arg[0]
        stack.append(x)
    else:
        print(stack.pop())
