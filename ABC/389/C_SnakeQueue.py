Q = int(input())

snakes = [0]
front = 0
for _ in range(Q):
    q, *x = input().split()
    if q == "1":
        l = int(x[0])
        snakes.append(snakes[-1] + l)
    elif q == "2":
        front += 1
    else:
        k = int(x[0])
        print(snakes[front + k - 1] - snakes[front])
