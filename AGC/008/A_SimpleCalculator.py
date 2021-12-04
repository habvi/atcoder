x, y = map(int, input().split())
if x == y == 0:
    print(0)
    exit()
if x <= y:
    print(min(y - x, abs(y + x) + 1))
    exit()

if not (x < 0 and y < 0 or x >= 0 and y >= 0):
    ans = abs(abs(x) - abs(y)) + 1
else:
    ans = abs(abs(x) - abs(y)) + 2

if y == 0:
    ans -= 1
print(ans)