from itertools import accumulate

n = int(input())

m = 10**6 + 2
ac = [0] * m

for _ in range(n):
    a, b = map(int, input().split())
    ac[a] += 1
    ac[b + 1] -= 1

print(max(accumulate(ac)))