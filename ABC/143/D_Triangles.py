from bisect import bisect, bisect_left
n = int(input())
L = list(map(int, input().split()))
L.sort()

cnt = 0
for i in range(n):
    for j in range(i+1,n):
        l = j + 1
        r = L[i] + L[j]
        br = bisect_left(L, r)
        cnt += br - l
print(cnt)