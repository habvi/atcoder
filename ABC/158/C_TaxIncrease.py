a, b = map(int, input().split())

for i in range(1, 1001):
    if a == i * 8 // 100 and b == i * 10 // 100:
        print(i)
        exit()

print(-1)