from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))

ac = list(accumulate(A[::-1]))[::-1] + [0]
ans = 0
for i, a in enumerate(A):
    ans += a * ac[i + 1]
print(ans)
