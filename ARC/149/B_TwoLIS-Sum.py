from bisect import bisect_left

def calc_lis(A):
    lis = [0]
    res = 0
    for a in A:
        if lis[-1] < a:
            lis.append(a)
            res += 1
        else:
            lis[bisect_left(lis, a)] = a
    return res


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ab = [(a, b) for a, b in zip(A, B)]
ab.sort()
ans = N + calc_lis([b for _, b in ab])

ab.sort(key=lambda x: x[1])
ans = max(ans, N + calc_lis([a for a, _ in ab]))
print(ans)
