A, B = map(int, input().split())

for i in reversed(range(1, B + 1)):
    total = 0
    for j in range(0, B + 1, i):
        total += (A <= j)
        if total == 2:
            print(i)
            exit()



# ---------------------------
A, B = map(int, input().split())

for i in reversed(range(1, B + 1)):
    r = B // i
    l = (A - 1) // i
    if r - l >= 2:
        print(i)
        exit()