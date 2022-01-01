x, y = map(int, input().split())
if x == y:
    print(x)
    exit()
for i in (0, 1, 2):
    if i not in (x, y):
        print(i)
        exit()