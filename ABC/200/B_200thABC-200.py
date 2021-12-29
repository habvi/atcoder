n, k = map(int, input().split())
for _ in range(k):
    if n % 200 == 0:
        n //= 200
    else:
        n = str(n) + '200'
        n = int(n)
print(n)