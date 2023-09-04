from collections import defaultdict

N, K = map(int, input().split())

ac = defaultdict(int)
day = set([0])
for _ in range(N):
    a, b = map(int, input().split())
    day.add(a)
    ac[0] += b
    ac[a] -= b

day = sorted(day)
for i in range(1, len(day)):
    ac[day[i]] += ac[day[i - 1]]

for d in day:
    if ac[d] <= K:
        print(d + 1)
        exit()
print(day[-1] + 1)