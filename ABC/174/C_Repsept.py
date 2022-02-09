K = int(input())
x = 7

for i in range(1, 10**6 + 1):
    x %= K
    if x == 0:
        print(i)
        exit()
    x = x * 10 + 7

print(-1)