n = int(input())

for p in range(30):
    x = 1
    for i in range(30):
        x *= 3
        if i == p:
            x += 1
    if x == n:
        print(p + 1)
        exit()
print(-1)