from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))

ans = 0
for a in A:
    base = a * 2
    ans += N - bisect_left(A, base)
print(ans)
