from bisect import bisect_left

N = int(input())

lis = [0]
minus = 0
for _ in range(N):
    c = int(input())
    if lis[-1] < c:
        lis.append(c)
        minus += 1
    else:
        lis[bisect_left(lis, c)] = c
print(N - minus)