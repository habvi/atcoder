n = int(input())
P = list(map(int, input().split()))
s = set()
now = 0
for p in P:
    s.add(p)
    while now in s:
        now += 1
    print(now)