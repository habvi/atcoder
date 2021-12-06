a = int(input())
for b in range(10, 10001):
    k = 1
    tot = 0
    for i in reversed(str(b)):
        tot += k * int(i)
        k *= b
    if a == tot:
        print(b)
        exit()
print(-1)