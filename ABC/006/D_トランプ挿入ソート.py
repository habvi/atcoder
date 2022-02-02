from bisect import bisect_left

n = int(input())

lis = [0]
for _ in range(n):
    c = int(input())
    if lis[-1] < c:
        lis.append(c)
    else:
        lis[bisect_left(lis, c)] = c

print(n - len(lis) + 1)