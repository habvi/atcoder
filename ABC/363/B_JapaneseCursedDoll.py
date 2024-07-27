N, T, P = map(int, input().split())
L = list(map(int, input().split()))

total = sum(l >= T for l in L)
if total >= P:
    print(0)
    exit()

for days in range(1, 101):
    L = [l + 1 for l in L]
    total = sum(l >= T for l in L)
    if total >= P:
        print(days)
        exit()
