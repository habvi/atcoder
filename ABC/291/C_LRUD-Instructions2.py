N = int(input())
S = input()

visited = set()
x, y = 0, 0
visited.add((x, y))
for s in S:
    if s == 'R':
        x += 1
    elif s == 'L':
        x -= 1
    elif s == 'U':
        y += 1
    else:
        y -= 1
    if (x, y) in visited:
        print("Yes")
        exit()
    visited.add((x, y))
print("No")