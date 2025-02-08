a, b, c = map(int, input().split())

for x, y, z in [(a, b, c), (a, c, b), (b, c, a)]:
    if x * y == z:
        print("Yes")
        exit()
print("No")
