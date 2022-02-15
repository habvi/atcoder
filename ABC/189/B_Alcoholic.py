n, x = map(int, input().split())
x *= 100

al = 0
for i in range(n):
    v, p = map(int, input().split())
    al += v * p
    if al > x:
        print(i + 1)
        exit()

print(-1)