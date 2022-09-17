def calc(a, b):
    diff = b - a
    if diff % 2:
        diff //= 2
        ll, lr = a, a + diff
        rl, rr = lr + 1, b
        return ll, lr, rl, rr, diff + 1, diff + 1
    else:
        diff //= 2
        ll, lr = a, a + diff
        rl, rr = lr + 1, b
        return ll, lr, rl, rr, diff + 1, diff


N = int(input())

col = None
l, r = 1, N
ll, lr, rl, rr, l_num, r_num = calc(l, r)
left, right = ll, lr
while col is None:
    print("?", 1, N, left, right)
    T = int(input())
    if T == 0:
        col = left
        break
    if l_num == r_num == 1:
        col = left + 1
        break
    if T == l_num:
        ll, lr, rl, rr, l_num, r_num = calc(rl, rr)
        left, right = ll, lr
    else:
        ll, lr, rl, rr, l_num, r_num = calc(left, right)
        left, right = ll, lr

row = None
l, r = 1, N
ll, lr, rl, rr, l_num, r_num = calc(l, r)
left, right = ll, lr
while row is None:
    print("?", left, right, 1, N)
    T = int(input())
    if T == 0:
        row = left
        break
    if l_num == r_num == 1:
        row = left + 1
        break
    if T == l_num:
        ll, lr, rl, rr, l_num, r_num = calc(rl, rr)
        left, right = ll, lr
    else:
        ll, lr, rl, rr, l_num, r_num = calc(left, right)
        left, right = ll, lr
print("!", row, col)