def is_prime(x):
    if x == 2:
        return True
    if x <= 1 or x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True


a, b, c, d = map(int, input().split())

count_ = 0
for i in range(a, b + 1):
    ok = False
    for j in range(c, d + 1):
        if is_prime(i + j):
            ok = True
            break
    count_ += (ok == True)

print('Aoki' if count_ == (b - a + 1) else 'Takahashi')