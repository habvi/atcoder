from bisect import bisect_left

n = int(input())

lis = [0]
ans = 0
for _ in range(n):
    w = int(input())

    if lis[-1] < w:
        lis.append(w)
        ans += 1
    else:
        lis[bisect_left(lis, w)] = w

print(ans)