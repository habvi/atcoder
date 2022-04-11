def solve(flag):
    ac = 0
    ans = 0
    for a in A:
        total = ac + a
        if flag == -1 and total <= 0:
            diff = abs(ac) + 1 - a
            ans += diff
            a += diff

        if flag == 1 and total >= 0:
            diff = ac + 1 + a
            ans += diff
            a -= diff

        ac += a
        flag *= -1
    return ans


n = int(input())
A = list(map(int, input().split()))

print(min(solve(1), solve(-1)))