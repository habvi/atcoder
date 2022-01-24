def f_xor(x):
    y = [x, 1, x + 1, 0]
    return y[x % 4]

a, b = map(int, input().split())
print(f_xor(b) ^ f_xor(a - 1))