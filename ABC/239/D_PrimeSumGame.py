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

for T in range(a, b + 1):
    inc = 0
    for A in range(c, d + 1):
        if not is_prime(T + A):
            inc += 1
    if inc == (d - c + 1):
        print('Takahashi')
        exit()

print('Aoki')