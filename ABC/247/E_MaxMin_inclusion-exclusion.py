def sigma(n):
    return n*(n + 1) // 2

def solve(A):
    global ans
    total = sigma(len(A))
    exclude_x, exclude_y = 0, 0
    exclude_xy = 0
    for a in A:
        if a == X:
            total -= sigma(exclude_x)
            exclude_x = 0
        else:
            exclude_x += 1

        if a == Y:
            total -= sigma(exclude_y)
            exclude_y = 0
        else:
            exclude_y += 1

        if a in (X, Y):
            total += sigma(exclude_xy)
            exclude_xy = 0
        else:
            exclude_xy += 1

    for pm, ex in zip((-1, -1, 1), (exclude_x, exclude_y, exclude_xy)):
        if ex:
            total += pm * sigma(ex)
    ans += total


n, X, Y = map(int, input().split())
A = list(map(int, input().split()))
 
B = []
new = []
for a in A:
    if Y <= a <= X:
        new.append(a)
    else:
        B.append(new)
        new = []
if new:
    B.append(new)

ans = 0
for C in B:
    solve(C)

print(ans)