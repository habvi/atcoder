S = input()
t = int(input())
q = 0
x, y = 0, 0
for s in S:
    if s == 'U':
        y += 1
    elif s == 'D':
        y -= 1
    elif s == 'L':
        x -= 1
    elif s == 'R':
        x += 1
    else:
        q += 1

d = abs(x) + abs(y)
if t == 1:
    print(d + q)
else:
    if d >= q:
        print(d - q)
        exit()
    
    if d % 2 == q % 2:
        print(0)
    else:
        print(1)