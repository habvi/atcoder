X = int(input())
price = [100 + i for i in range(6)]

dp = 1
for i in range(X // 100 + 1):
    add_ = 0
    for p in price:
        add_ |= dp << p
    dp |= add_

print(1 if dp >> X & 1 else 0)