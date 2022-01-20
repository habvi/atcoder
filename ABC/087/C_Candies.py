from itertools import accumulate
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ac = list(accumulate(a))
bc = list(accumulate(b[::-1]))[::-1]

ans = 0
for a, b in zip(ac, bc):
    ans = max(ans, a + b)
print(ans)