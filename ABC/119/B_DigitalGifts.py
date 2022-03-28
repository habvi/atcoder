n = int(input())
BTC = 380000

total = 0
for _ in range(n):
    x, u = input().split()
    x = float(x)
    total += (x if u == 'JPY' else x * BTC)
print(total)