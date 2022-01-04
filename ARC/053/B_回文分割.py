from collections import Counter
s = input()
c = Counter(s)

ev, od = 0, 0
for k, v in c.items():
    if v % 2 == 1:
        ev += v - 1
        od += 1
    else:
        ev += v

if not od:
    print(len(s))
else:
    print(ev // 2 // od  * 2 + 1)