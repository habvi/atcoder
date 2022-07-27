def sep_list(A):
    res = []
    for a in A:
        if Y <= a <= X:
            res.append(a)
        else:
            if res:
                yield res
                res = []
    if res:
        yield res


N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for lis in sep_list(A):
    nearest_mn = 0
    nearest_mx = 0
    for i, a in enumerate(lis):
        if a == X:
            nearest_mx = i + 1
        if a == Y:
            nearest_mn = i + 1

        if a == X:
            ans += nearest_mn
        elif a == Y:
            ans += nearest_mx
        else:
            ans += min(nearest_mn, nearest_mx)
print(ans)