x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

ans = []
if x1 == x2:
    ans.append(x3)
elif x2 == x3:
    ans.append(x1)
else:
    ans.append(x2)

if y1 == y2:
    ans.append(y3)
elif y2 == y3:
    ans.append(y1)
else:
    ans.append(y2)

print(*ans)