from collections import Counter

n = int(input())
A = list(map(int, input().split()))

R = [*range(400, 3201, 400), float('inf')]

rate = Counter()
for a in A:
    for i, r in enumerate(R):
        if a < r:
            rate[i] += 1
            break

num = len(rate)
if not (over := rate[8]):
    print(num, num)
else:
    other = num - 1
    print(max(1, other), other + over)