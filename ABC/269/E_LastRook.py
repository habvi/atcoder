def is_ok(l, r):
    T = int(input())
    return T != (r - l) 

def bisect1(l, r):
    while abs(r - l) > 1:
        mid = (r + l) // 2
        print('?', l, mid - 1, 1, N)
        if is_ok(l, mid):
            r = mid
        else:
            l = mid
    return r - 1

def bisect2(l, r):
    while abs(r - l) > 1:
        mid = (r + l) // 2
        print('?', 1, N, l, mid - 1)
        if is_ok(l, mid):
            r = mid
        else:
            l = mid
    return r - 1


N = int(input())

row = bisect1(1, N + 1)
col = bisect2(1, N + 1)
print("!", row, col)