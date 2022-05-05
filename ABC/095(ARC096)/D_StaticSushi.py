def calc_sum(xv, start):
    one = [0]
    two = [0]
    pre = start
    for x, v in xv:
        one.append(one[-1] + v - abs(pre - x))
        two.append(two[-1] + v - abs((pre - x) * 2))
        pre = x
    return one, two

def calc_max(one, two):
    mx1, mx2 = [], []
    now1, now2 = 0, 0
    for x, y in zip(one, two):
        now1 = max(now1, x)
        now2 = max(now2, y)
        mx1.append(now1)
        mx2.append(now2)

    mx = 0
    for i in range(n + 1):
        mx = max(mx, mx1[i] + mx2[~i])
    return mx


n, C = map(int, input().split())
xv = [tuple(map(int, input().split())) for _ in range(n)]

right1, right2 = calc_sum(xv, 0)
left1, left2 = calc_sum(xv[::-1], C)

ans = max(calc_max(right1, left2), calc_max(left1, right2))
print(ans)