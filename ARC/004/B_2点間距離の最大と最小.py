n = int(input())
d = [int(input()) for _ in range(n)]
print(sum(d))

d.sort()
sm = sum(d[:-1])
if d[-1] > sm:
    print(d[-1] - sm)
else:
    print(0)