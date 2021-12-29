n, m = map(int, input().split())
ev, od = 0, 0
for _ in range(n):
    s = input()
    if s.count('1') % 2 == 0:
        ev += 1
    else:
        od += 1
print(ev * od)