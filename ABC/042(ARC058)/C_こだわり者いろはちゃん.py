n, k = map(int, input().split())
D = input().split()
s = set(D)

while True:
    if not set(str(n)) & s:
        print(n)
        exit()
    n += 1